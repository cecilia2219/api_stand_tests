import configuration
import requests
import data




def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, # Concatenación de URL base y ruta.
                         json=body, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.

response = post_new_user(data.user_body)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
