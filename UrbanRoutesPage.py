from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import address_from, address_to, phone_number,card_number, card_code, message_for_driver, urban_routes_url
from locators import UrbanRoutesLocators
from get_code import retrieve_phone_code

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesLocators()

    def test_set_from(self, address):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.locators.from_field))
        element.send_keys(address)

        assert element.get_attribute(
            "value") == address, f"Expected '{address}', but got '{element.get_attribute('value')}'"

    def test_set_to(self, address):
        self.driver.find_element(*self.locators.to_field).send_keys(address)

        to_element = self.driver.find_element(*self.locators.to_field)
        assert to_element.get_attribute(
            "value") == address, f"Expected '{address}', but got '{to_element.get_attribute('value')}'"

    def test_select_comfort(self):
        wait = WebDriverWait(self.driver, 10)
        comfort_element = wait.until(EC.element_to_be_clickable(self.locators.locator_comfort))
        comfort_element.click()


    def test_fill_out_phone_form(self):
        self.driver.find_element(*self.locators.click_phone_number).click()
        self.driver.find_element(*self.locators.phone_input_locator).send_keys(phone_number)
        self.driver.find_element(*self.locators.button_next_phone).click()

        phone_input = self.driver.find_element(*self.locators.phone_input_locator)
        assert phone_input.get_attribute(
            "value") == phone_number, f"Expected phone number '{phone_number}', but got '{phone_input.get_attribute('value')}'"

    def test_confirm_phone_code(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.locators.phone_number_code))
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.locators.phone_number_code).send_keys(code)
        self.driver.find_element(*self.locators.confirm_code_phone).click()

        code_input = self.driver.find_element(*self.locators.phone_number_code)
        assert code_input.get_attribute(
            "value") == code, f"Expected code '{code}', but got '{code_input.get_attribute('value')}'"

    def test_add_credit_card(self):
        self.driver.find_element(*self.locators.payment_method).click()
        self.driver.find_element(*self.locators.add_card).click()
        self.driver.find_element(*self.locators.field_number_card).send_keys(card_number)
        self.driver.find_element(*self.locators.field_code_card).send_keys(card_code)
        self.driver.find_element(*self.locators.field_code_card).send_keys(Keys.TAB)
        self.driver.find_element(*self.locators.button_add_card).click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.locators.close_payment_button)).click()


    def test_write_message(self):
        self.driver.find_element(*self.locators.message_console).send_keys(message_for_driver)

        message_input = self.driver.find_element(*self.locators.message_console)
        assert message_input.get_attribute(
            "value") == message_for_driver, f"Expected message '{message_for_driver}', but got '{message_input.get_attribute('value')}'"

    def test_request_blanket_and_tissues(self):
        self.driver.find_element(*self.locators.request_blankets_scarves).click()


    def test_request_ice_cream(self):
        for _ in range(2):
            self.driver.find_element(*self.locators.request_helado).click()


    def test_open_taxi_modal(self):
        self.driver.find_element(*self.locators.request_taxi).click()

        # Assert para verificar que el modal se abrió (puedes ajustar esto según tu lógica)
        assert self.driver.find_element(*self.locators.request_taxi).is_displayed(), "Taxi modal did not open."

    def test_wait_for_driver_info(self):
        wait = WebDriverWait(self.driver, 50)
        name_driver_element = wait.until(EC.visibility_of_element_located(self.locators.name_driver))
        driver_name = name_driver_element.text

        assert driver_name, "Driver name was not retrieved."

        element_time_of_waiting = wait.until(EC.visibility_of_element_located(self.locators.time_of_waiting))
        driver_time_wait = element_time_of_waiting.text

        assert driver_time_wait, "Driver waiting time was not retrieved."

        element_number_of_trip = wait.until(EC.visibility_of_element_located(self.locators.number_of_trip))
        driver_number_trip = element_number_of_trip.text

        assert driver_number_trip, "Driver trip number was not retrieved."

    def test_verify_information_trip(self):
        wait = WebDriverWait(self.driver, 50)
        self.driver.find_element(*self.locators.detail_button).click()

        pickup_location_text = wait.until(EC.visibility_of_element_located(self.locators.pickup_location)).text
        droppoff_location_text = wait.until(EC.visibility_of_element_located(self.locators.droppoff_location)).text
        payment_method_text = wait.until(EC.visibility_of_element_located(self.locators.payment_method_locator)).text

        from_field_text = wait.until(EC.visibility_of_element_located(self.locators.from_field)).get_attribute("value")
        to_field_text = wait.until(EC.visibility_of_element_located(self.locators.to_field)).get_attribute("value")

        assert pickup_location_text == from_field_text, f"Pickup location '{pickup_location_text}' does not match from field '{from_field_text}'"
        assert droppoff_location_text == to_field_text, f"Droppoff location '{droppoff_location_text}' does not match to field '{to_field_text}'"
        assert payment_method_text == "Tarjeta", f"Payment method '{payment_method_text}' is not 'Tarjeta'"