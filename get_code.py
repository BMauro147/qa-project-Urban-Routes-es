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
