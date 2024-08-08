import pytest
import allure
import requests


def Create_Token():
    base_url = "https://restful-booker.herokuapp.com/auth"
    Headers = {'Content-Type': 'application/json'}
    Payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=base_url, headers=Headers, json=Payload)
    data = response.json()
    print(data['token'])
    return data["token"]


def Create_Booking():
    base_url = "https://restful-booker.herokuapp.com/booking"
    Headers = {'Content-Type': 'application/json'}
    payload ={
    "firstname" : "Mia",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

    response = requests.post(url=base_url, headers=Headers, json=payload)
    data = response.json()
    print(data)
    booking_id = data["bookingid"]
    return str(booking_id)


def test_Patch_With_Positive():
    base_url = "https://restful-booker.herokuapp.com/booking/"+Create_Booking()
    Headers ={"Content-Type": "application/json",
              "Cookie": "token="+Create_Token()}
    payload = {
        "firstname": "Mohammad",
        "lastname": "Zayn"
    }

    response = requests.patch(url=base_url, headers=Headers, json=payload)
    data = response.json()
    print(data["firstname"])
    print(data["lastname"])