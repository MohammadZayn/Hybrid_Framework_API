import pytest
import allure
import requests


# create token
def Generate_Token():
    URL = "https://restful-booker.herokuapp.com/auth"
    HEADER = {"Content-Type": "application/json"}
    PAYLOAD = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=URL, headers=HEADER, json=PAYLOAD)
    print(response.json())
    token = response.json()["token"]
    return token


# create new booking
def Create_Booking():
    """ URL
    Method - Post
    Header - Content-Type = application/json
    Payload/Data/Body - Dict/Json
    Auth - Not required """
    URL = "https://restful-booker.herokuapp.com"
    PATH_URL = "/booking"
    base_url = URL + PATH_URL
    HEADERS = {"Content-Type": "application/json"}
    Payload = {
        "firstname": "Sara",
        "lastname": "Shaik",
        "totalprice": 4000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-011",
            "checkout": "2024-05-13"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=base_url, headers=HEADERS, json=Payload)
    assert response_data.status_code == 200
    ''' Response Body Verification
        Headers
        Status Code
        Json Schema Validation
        Time Response'''
    data = response_data.json()
    booking_id = data["bookingid"]
    return booking_id


# create a put request
def test_Put_Request_Positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(Create_Booking())
    put_url = base_url+base_path

    cookie = "token=" + Generate_Token()

    HEADERS = {"Application-Type": "application/json",
               "Cookie": cookie}
    payload = {
        "firstname": "Mohammad",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.put(url=put_url, headers=HEADERS, json=payload)
    assert response_data.status_code == 200
    data = response_data.json()
    assert data["firstname"] == 'Mohammad'

def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = Create_Booking()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + Generate_Token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)
    response = requests.delete(url=DELETE_URL, headers=headers)