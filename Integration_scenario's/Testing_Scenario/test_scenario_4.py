import pytest
import allure

@allure.title("#Test_Case -4")
@allure.description("Create a BOOKING, Delete It.")
@allure.tag("Integration", "#4", "TestCase")
@allure.label("Owner", "Mohammad_Zain")
@allure.testcase("Integration_Testing_4")
def test_create_booking_delete(Delete_Booking):
    booking_id = Delete_Booking
    print("booking_id")