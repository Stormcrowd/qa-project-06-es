import sender_stand_request
import data


# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):

    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


# Función de prueba positiva
def positive_assert(first_name):

    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

    users_table_response = sender_stand_request.get_users_table()


#Pendiente de cambiar el str
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    assert users_table_response.text.count(str_user) == 1
    assert user_response.json()["message"] == 'El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud'


#PRUEBA NEGATIVA
# Función de prueba negativa
def negative_assert_symbol(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)

    # Comprueba si la variable "response" almacena el resultado de la solicitud.
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el código 400.
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

# Función de prueba negativa
# La respuesta contiene el siguiente mensaje de error: "No se han enviado todos los parámetros requeridos"
def negative_assert_no_firstname(user_body):
    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"
# Prueba 1
def test_create_user_1_letter_in_first_name_get_success_response():
    positive_assert(data.kit_1_letter)

# Prueba 2
def test_create_user_511_letter_in_first_name_get_success_response():
    positive_assert(data.kit_2_letter)

# Prueba 5
def test_create_user_1_letter_in_first_name_get_error_response():
    positive_assert(data.kit_5_letter)


# Prueba 6
def test_create_user_has_space_in_first_name_get_error_response():
    positive_assert(data.kit_6_letter)

# Prueba 7
def test_create_user_has_number_in_first_name_get_error_response():
    positive_assert(data.kit_7_letter)

#Prueba 4
def test_create_user_512_letter_in_first_name_get_success_response():
    negative_assert_symbol(data.kit_4_letter)



# Prueba 8. Error
# La solicitud no contiene el parámetro "firstName"  ---> Lo estoy eliminando en el envio (perdido).
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    user_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)


# Prueba 3. Error
# El parámetro "firstName" contiene un string vacío
def test_create_user_empty_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body("")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

# Prueba 9. Error
# El tipo del parámetro "firstName" es un número
def test_create_user_number_type_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(12)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400