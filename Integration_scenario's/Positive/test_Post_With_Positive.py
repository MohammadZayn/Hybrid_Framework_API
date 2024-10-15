import pytest
import allure
import requests

@allure.title("#TC - 1 Creating a booking slot with all correct parameters")
@allure.description("This test case will help you to create the booking slot in a hotel")
@allure.id("#TestCase - 1")
@allure.tag("CRUD", "Positive", "Creating")
def test_Create_Booking_With_Exact_Details():
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
        "totalprice": 2000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-011",
            "checkout": "2024-05-13"
        },
        "additionalneeds": "Breakfast"
    }
    responsedata = requests.post(url=base_url, headers=HEADERS,json=Payload)
    assert responsedata.status_code == 200
    print(responsedata.json())
    ''' Response Body Verification
        Headers
        Status Code
        Json Schema Validation
        Time Response'''
    data = responsedata.json()
    assert data["bookingid"] is not None
    assert type(data["bookingid"]) is int
    assert data["bookingid"] > 0
    firstname = data["booking"]["firstname"]
    assert firstname == 'Mohammad', "Yes Name fetched successfully"
    assert data["booking"]["bookingdates"]["checkin"] == "2024-03-11"
