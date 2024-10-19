# Urban Routes Automation Tests

## Autor
**Jesús Mauro Becerra Galván** 

## Proyecto
**Urban Routes Automation Tests**

## Sprint
**Sprint 8 Pruebas Automatizadas** 

Este repositorio contiene pruebas automatizadas para comprobar la funcionalidad de la aplicación **Urban Routes**. Las pruebas están diseñadas para cubrir el proceso completo de solicitar un taxi, asegurando que todas las funcionalidades esenciales estén correctamente implementadas.

## Requisitos

Para ejecutar las pruebas, asegúrate de tener instalado lo siguiente:

- Python 3.x
- Selenium
- Un controlador de navegador (por ejemplo, ChromeDriver para Google Chrome)

## Estructura del Proyecto

- `main.py`: Contiene la implementación de las pruebas y la lógica de la página de Urban Routes.
- `data.py`: Archivo que contiene las variables necesarias para las pruebas, como direcciones y datos de contacto.

## Funcionalidades Probadas

Las pruebas automatizadas cubren las siguientes acciones:

1. **Configurar la dirección**: Se establece la dirección de origen y destino.
2. **Seleccionar la tarifa Comfort**: Se selecciona la tarifa preferida para el viaje.
3. **Rellenar el número de teléfono**: Se ingresa el número de teléfono del usuario.
4. **Agregar una tarjeta de crédito**: Se agrega la información de una tarjeta de crédito, asegurándose de que el campo CVV pierda el enfoque correctamente.
5. **Escribir un mensaje para el controlador**: Se envía un mensaje personalizado al conductor.
6. **Pedir una manta y pañuelos**: Se solicita una manta y pañuelos durante el viaje.
7. **Pedir helados**: Se piden dos helados.
8. **Abrir el modal de búsqueda de taxi**: Se inicia la búsqueda de un taxi.
9. **Esperar información del conductor**: Se espera hasta que la información del conductor esté disponible.

## Ejecución de Pruebas

Para ejecutar las pruebas, asegúrate de tener todos los requisitos instalados y corre el siguiente comando en la terminal:

```bash
python main.py

## Implementación

El archivo `main.py` contiene las clases `UrbanRoutesPage` y `TestUrbanRoutes`, donde:

- **UrbanRoutesPage**: Define los localizadores y métodos necesarios para interactuar con la página.
  - **Localizadores**:
    - `from_field`
    - `to_field`
    - `button_taxi`
    - `locator_comfort`
    - `click_phone_number`
    - `phone_input_locator`
    - `button_next_phone`
    - `phone_number_code`
    - `confirm_code_phone`
    - `payment_method`
    - `add_card`
    - `field_number_card`
    - `field_code_card`
    - `button_add_card`
    - `message_console`
    - `request_blankets_scarves`
    - `request_helado`
    - `request_taxi`
  
  - **Métodos**:
    - `set_from(address)`
    - `set_to(address)`
    - `select_comfort()`
    - `fill_out_phone_form()`
    - `confirm_phone_code()`
    - `add_credit_card()`
    - `write_message()`
    - `request_blanket_and_tissues()`
    - `request_ice_cream()`
    - `open_taxi_modal()`
    - `wait_for_driver_info()`

- **TestUrbanRoutes**: Contiene las pruebas automatizadas que verifican la funcionalidad de la aplicación.

### Ejemplo de Código

A continuación se muestra un ejemplo de cómo se configuran y ejecutan las pruebas:

```python
class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # Configuración del driver de Selenium
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        # Inicia la prueba configurando la dirección y seleccionando la tarifa
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from("Dirección de origen")
        routes_page.set_to("Dirección de destino")
        routes_page.select_comfort()
        …
## Contribuciones
Si deseas contribuir a este proyecto, no dudes en enviar un pull request o abrir un issue para discutir mejoras. Todas las contribuciones son bienvenidas.
