import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
from data import address_from, address_to, phone_number,card_number, card_code, message_for_driver, urban_routes_url


# no modificar
import json
import time
from selenium.common import WebDriverException

def retrieve_phone_code(driver, retries=10, wait_time=1) -> str:
    """Devuelve un número de confirmación de teléfono como un string.
    Úsalo cuando la aplicación espere el código de confirmación para tus pruebas.
    El código solo se puede obtener después de haberlo solicitado en la aplicación."""

    code = None
    for _ in range(retries):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                                {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
                if code:  # Si se encontró el código, salir del bucle
                    break
        except WebDriverException as e:
            print(f"Error al acceder a los logs: {e}")  # Registro del error
            time.sleep(wait_time)
            continue

        if code:
            return code
        time.sleep(wait_time)

    raise Exception("No se encontró el código de confirmación del teléfono.\n"
                    "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")



class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_taxi = (By.CSS_SELECTOR, "button.button:nth-child(3)")
    locator_comfort = (By.CSS_SELECTOR, "div.tcard:nth-child(5) > div:nth-child(2) > img:nth-child(1)")
    click_phone_number =(By.CSS_SELECTOR, ".np-button")
    phone_input_locator = (By.CSS_SELECTOR, "#phone")
    button_next_phone = (By.CSS_SELECTOR, ".number-picker > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(2) > button:nth-child(1)")
    phone_number_code = (By.ID, "code")
    confirm_code_phone = (By.CSS_SELECTOR, "div.active:nth-child(2) > form:nth-child(3) > div:nth-child(2) > button:nth-child(1)")
    payment_method = (By.CSS_SELECTOR, ".pp-button")
    add_card = (By.CSS_SELECTOR,".pp-plus")
    field_number_card = (By.CSS_SELECTOR, "#number")
    field_code_card = (By.CSS_SELECTOR,".card-code-input > input:nth-child(1)")
    button_add_card = (By.CSS_SELECTOR,".pp-buttons > button:nth-child(1)")
    message_console = (By.CSS_SELECTOR,".form > div:nth-child(3) > div:nth-child(1) > label:nth-child(2)")
    request_blankets_scarves = (By.CSS_SELECTOR, "div.r-type-switch:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)")
    request_helado = (By.CSS_SELECTOR, "div.sub:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3)")
    request_taxi = (By.CSS_SELECTOR, ".smart-button-main")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, address):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(self.from_field))
        element.send_keys(address)

    def set_to(self, address):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def select_comfort(self):
        wait = WebDriverWait(self.driver, 10)
        comfort_element = wait.until(EC.element_to_be_clickable(self.locator_comfort))
        comfort_element.click()

    def fill_out_phone_form(self):
        self.driver.find_element(*self.click_phone_number).click()
        self.driver.find_element(*self.phone_input_locator).send_keys(phone_number)
        self.driver.find_element(*self.button_next_phone).click()

    def confirm_phone_code(self):
        wait = WebDriverWait(self.driver, 10)  # Aumenté el tiempo de espera a 20 segundos
        wait.until(EC.visibility_of_element_located(self.phone_number_code))
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.phone_number_code).send_keys(code)
        self.driver.find_element(*self.confirm_code_phone).click()

    def add_credit_card(self):
        self.driver.find_element(*self.payment_method).click()
        self.driver.find_element(*self.add_card).click()
        self.driver.find_element(*self.field_number_card).send_keys(card_number)
        self.driver.find_element(*self.field_code_card).send_keys(card_code)
        self.driver.find_element(*self.field_code_card).send_keys(Keys.TAB)  # Cambiar el enfoque
        self.driver.find_element(*self.button_add_card).click()

    def write_message(self):
        self.driver.find_element(*self.message_console).send_keys(message_for_driver)

    def request_blanket_and_tissues(self):
        self.driver.find_element(*self.request_blankets_scarves).click()
        time.sleep(1)

    def request_ice_cream(self):
        for _ in range(2):
            self.driver.find_element(*self.request_helado).click()

    def open_taxi_modal(self):
        self.driver.find_element(*self.request_taxi).click()

    def wait_for_driver_info(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.driver_info)
        )

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = Options()  # Define aquí chrome_options
        chrome_options.add_argument("--headless")  # Opcional
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Configurar la dirección
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(routes_page.button_taxi)
        )

        routes_page.driver.find_element(*routes_page.button_taxi).click()
        time.sleep(2)
        # Seleccionar la tarifa Comfort
        routes_page.select_comfort()

        # Rellenar el número de teléfono
        routes_page.fill_out_phone_form()
        routes_page.confirm_phone_code()

        # Agregar una tarjeta de crédito
        routes_page.add_credit_card()

        # Escribir un mensaje para el controlador
        routes_page.write_message()

        # Pedir una manta y pañuelos
        routes_page.request_blanket_and_tissues()

        # Pedir 2 helados
        routes_page.request_ice_cream()

        # Abrir el modal para buscar un taxi
        routes_page.open_taxi_modal()

        # Esperar a que aparezca la información del conductor
        routes_page.wait_for_driver_info()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
""" Hola que tal, como comentario trate de realizar hasta donde pude el código, la parte donde me confunde es
 al obtener el código para el numero de telefono, estuve investigando como realizar esto, pero no lo logré,
 el problema inicia con esto 
 def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

ya que desired_capabilities me lo muestra como error en python y si bien menciona no modificar el código lo modifique para 
poder avanzar en las pruebas, si bien avance hasta el paso de obtener el código pero aquí es donde mi código ya no funciona
de igual manera si tienes alguna ayuda u orientación para que el código funcione sería de mucha ayuda"""