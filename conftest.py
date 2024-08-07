import pytest
import requests


@pytest.fixture
def Create_Token():
    base_url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    body = {"username": "admin", "password": "password123"}
    response = requests.post(url=base_url, headers=headers, json=body)
    response.raise_for_status()  # Ensure we raise an error for bad status codes
    data = response.json()
    return data["token"]


@pytest.fixture
def Create_Booking():
    print("Create Booking Testcase")
    base_url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    body = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-01-02"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=base_url, headers=headers, json=body)
    response.raise_for_status()
    data = response.json()
    return str(data["bookingid"])


@pytest.fixture
def Patch_Booking(Create_Booking, Create_Token):
    base_url = "https://restful-booker.herokuapp.com/booking/" + Create_Booking
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={Create_Token}"
    }
    body = {
        "firstname": "Jane",
        "lastname": "Doe",
        "totalprice": 222,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2022-02-01",
            "checkout": "2022-02-02"
        },
        "additionalneeds": "Lunch"
    }
    response = requests.patch(url=base_url, headers=headers, json=body)
    response.raise_for_status()
    print(Create_Booking)
    print(Create_Token)
    data = response.json()
    return data


@pytest.fixture
def Delete_Booking(Create_Booking, Create_Token):
    booking_id = Create_Booking
    base_url = "https://restful-booker.herokuapp.com/booking/" + Create_Booking
    header = {
        "Content-Type": "application/json",
        "Cookie": f"token={Create_Token}"
    }
    response = requests.delete(url=base_url, headers=header)
    response.raise_for_status()  # Ensure we raise an error for bad status codes
    return booking_id


@pytest.fixture()
def Existing_Booking_ID():
    baseurl = "https://restful-booker.herokuapp.com/booking"
    response = requests.get(url=baseurl)
    response.raise_for_status()  # Ensure we raise an error for bad status codes
    Booking_ID_list = response.json()
    return Booking_ID_list


@pytest.fixture()
def Get_Booking_ID_Info():
    def _get_info(Id_Details):
        baseurl = f"https://restful-booker.herokuapp.com/booking/{Id_Details}"
        response = requests.get(url=baseurl)
        response.raise_for_status()
        details = response.json()
        return details

    return _get_info


@pytest.fixture
def Create_Booking_With_Invalid_Payload():
    base_url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    body = {
        "firstname": "Sara",
        "lastname": "Brown",
        "totalprice": Mohammad,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-01-02"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=base_url, headers=headers, json=body)
    response.raise_for_status()
    details = response.json()
    return response


@pytest.fixture
def Put_Booking(Create_Token, ):
    def _get_info(baseurl):
        base_url = baseurl
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={Create_Token}"
        }
        body = {
            "firstname": "Jane",
            "lastname": "Doe",
            "totalprice": 222,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2022-02-01",
                "checkout": "2022-02-02"
            },
            "additionalneeds": "Lunch"
        }
        response = requests.patch(url=base_url, headers=headers, json=body)
        response.raise_for_status()
        return response
    return _get_info
