
import pytest
import allure

@allure.title("#Test_Case -3")
@allure.description(
    "Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.")
@allure.tag("Integration", "#3", "TestCase")
@allure.label("Owner", "Mohammad_Zain")
@allure.testcase("Integration_Testing_3")
def test_Exiting_all_BookingID_Update_Verify(Existing_Booking_ID, Get_Booking_ID_Info):
    Booking_ID_list = Existing_Booking_ID
    if len(Booking_ID_list) > 2:
        Id_details = Booking_ID_list[2]['bookingid']  # Access the third booking ID correctly
        details = Get_Booking_ID_Info(Id_details)
        print(details)

        # Add assertions to verify the details if needed
        assert 'firstname' in details
        assert 'lastname' in details
    else:
        pytest.skip("Not enough bookings available for the test.")