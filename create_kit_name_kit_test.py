import sender_stand_request
import data


# Positive result, 201
def positive_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

#Negative result,400
def negative_assert_code_400(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    assert response.status_code == 400


#Prueba 1, min character
def test_1():
    positive_assert(data.kit_1_letter)


#Prueba 2, max character
def test_2():
    positive_assert(data.kit_2_letter)


#Prueba 3, min character -1
def test_3():
    negative_assert_code_400(data.kit_3_letter)   #CURRENT: FAILED , 201 CODE


#Prueba 4, max caracter +1
def test_4():
    negative_assert_code_400(data.kit_4_letter)   #CURRENT: FAILED , 201 CODE


#Prueba 5, Special character
def test_5():
    positive_assert(data.kit_5_letter)


#Prueba 6, Space character
def test_6():
    positive_assert(data.kit_6_letter)


#Prueba 7, string number
def test_7():
    positive_assert(data.kit_7_letter)


#Prueba 8, Null
def test_8():
    negative_assert_code_400(data.kit_8_letter)  #500 error


#Prueba  9, Int
def test_9():
    negative_assert_code_400(data.kit_9_letter)  #CURRENT: FAILED , 201 CODE

