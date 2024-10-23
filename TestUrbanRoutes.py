import data
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import address_from, address_to, phone_number,card_number, card_code, message_for_driver, urban_routes_url
from UrbanRoutesPage import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        # Estos son para colab :)
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--window-size=1920x1080")
        # chrome_options.headless = True
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Configurar la dirección
        routes_page.test_set_from(address_from)
        routes_page.test_set_to(address_to)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(routes_page.locators.button_taxi)
        )

        routes_page.driver.find_element(*routes_page.locators.button_taxi).click()

        # Seleccionar la tarifa Comfort
        routes_page.test_select_comfort()

        # Rellenar el número de teléfono
        routes_page.test_fill_out_phone_form()
        routes_page.test_confirm_phone_code()

        # Agregar una tarjeta de crédito
        routes_page.test_add_credit_card()

        # Escribir un mensaje para el controlador
        routes_page.test_write_message()

        # Pedir una manta y pañuelos
        routes_page.test_request_blanket_and_tissues()

        # Pedir 2 helados
        routes_page.test_request_ice_cream()

        # Abrir el modal para buscar un taxi
        routes_page.test_open_taxi_modal()

        # Esperar a que aparezca la información del conductor
        routes_page.test_wait_for_driver_info()

        #Verifica que la información del viaje sea correcta
        routes_page.test_verify_information_trip()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()