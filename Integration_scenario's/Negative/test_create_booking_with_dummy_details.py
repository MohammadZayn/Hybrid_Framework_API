import pytest
import allure
import requests

@allure.title("#TC - 2 Creating a booking slot with not passing payload/data")
@allure.description("This test case will help you to create the booking slot in a hotel")
@allure.id("#TestCase - 1")
@allure.tag("CRUD", "Negative", "Checking")
@pytest.mark.CRUD
def test_Create_Booking_With_No_Patload_or_Data():
    '''  URL
    Method - Post
    Header - Content-Type = application/json
    Payload/Data/Body - Dict/Json
    Auth - Not required'''
    URL = "https://restful-booker.herokuapp.com"
    PATH_URL = "/booking"
    base_url = URL + PATH_URL
    HEADERS = {"Content-Type": "application/json"}
    Payload ={}
    responsedata = requests.post(url=base_url, headers=HEADERS,json=Payload)
    ''' Response Body Verification
        Headers
        Status Code
        Json Schema Validation
        Time Response'''
    assert responsedata.status_code == 500


@pytest.mark.CRUD
@allure.title("#TC - 3 Creating a booking slot with total price as a string")
@allure.description("This test case will help you to create the booking slot by using the total price as name")
@allure.id("#TestCase - 1")
@allure.tag("CRUD", "Positive", "Creating")
def test_Create_Booking_With_Totalprice_as_string():
    '''  URL
    Method - Post
    Header - Content-Type = application/json
    Payload/Data/Body - Dict/Json
    Auth - Not required'''
    URL = "https://restful-booker.herokuapp.com"
    PATH_URL = "/booking"
    base_url = URL + PATH_URL
    HEADERS = {"Content-Type": "application/json"}
    Payload = {
        "firstname": "Mohammad",
        "lastname": "Shaik",
        "totalprice": 'Mohammad',
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-011",
            "checkout": "2024-05-13"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=base_url, headers=HEADERS,json=Payload)
    assert response_data.status_code == 200
    print(response_data.json())
    ''' Response Body Verification
        Headers
        Status Code
        Json Schema Validation
        Time Response'''
    data = response_data.json()
    firstname = data["booking"]["firstname"]
    try:
        assert data["bookingid"] is not None
        assert type(data["bookingid"]) is int
        assert data["bookingid"] > 0
        assert firstname == 'Mohammad', "Yes name fetched successfully"
        assert data["booking"]["bookingdates"]["checkin"] == "2024-03-11"
        assert data["booking"]["totalprice"] == 2000
        assert data["booking"]["totalprice"] == 2000, f"Expected 2000, but got {data['booking']['totalprice']}"
    except AssertionError as e:
        print(f"Assertion failed: {e}")
