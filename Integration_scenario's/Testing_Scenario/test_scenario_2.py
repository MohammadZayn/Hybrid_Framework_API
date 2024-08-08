import pytest
import requests
import allure


@allure.title("#Test_Case -2")
@allure.description(
    "Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.")
@allure.tag("Integration", "#2", "TestCase")
@allure.label("Owner", "Mohammad_Zain")
@allure.testcase("Integration_Testing_2")
def test_create_and_delete_booking(Create_Booking, Delete_Booking):
    booking_id = Create_Booking
    # Verify the booking was created
    response = requests.get("https://restful-booker.herokuapp.com/booking/"+booking_id)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Verify the booking was deleted
    deleted_booking_id = Delete_Booking
    response = requests.get(f"https://restful-booker.herokuapp.com/booking/{deleted_booking_id}")
    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"