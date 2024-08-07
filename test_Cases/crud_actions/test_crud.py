# Create Token
# Create Booking Id
# Update the Booking(Put) - BookingID, Token
# Delete the Booking


# Verify that created booking id when we update we are able to update it and delete it also


import allure
from Source_Content.All_in_one import *

class TestCRUDBooking:
    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description("Verify that Full Update with the booking ID and Token is working.")
    @allure.tag("Integration", "#1", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_1")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = R.patch_put_delete_url(booking_id=booking_id)
        response = R.put_requests(url=put_url, headers=R.common_header_put_delete_patch_cookie(token=token),
                                  payload=R.create_booking_payload(), auth=None, in_json=False)
        # Verification here & more
        R.verify_response_key(response.json()["firstname"], "Amit")
        R.verify_response_key(response.json()["lastname"], "Brown")
        R.verify_http_status_code(response_data=response, expect_data=200)

    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description("Verify booking gets deleted with the booking ID and Token.")
    @allure.tag("Integration", "#2", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_2")
    def test_delete_booking_id(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = R.patch_put_delete_url(booking_id=booking_id)
        response = R.delete_requests(url=delete_url,headers=R.common_header_put_delete_patch_cookie(token=token),
                                     auth=None,in_json=False)
        R.verify_response_delete(response=response.text)
        R.verify_http_status_code(response_data=response, expect_data=201)
