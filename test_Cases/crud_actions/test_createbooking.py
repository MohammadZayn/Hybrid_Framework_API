import allure
import pytest
from Source_Content.All.All_in_one import *

class Test_Create_Booking:
    @allure.title("#Test_Case -1")
    @allure.description("Verify that Create Booking -> Patch Request - Verify that firstName is updated.")
    @allure.tag("Integration", "#1", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_1")
    def test_create_booking(self):
        print("Create Booking Testcase")
        response = Crud_operation.post_request(url=R.create_booking_url(),auth=None,headers=R.common_headers_json(),
                                               payload=R.create_booking_payload(), in_json=False)
        R.verify_http_status_code(response_data=response, expect_data=200)
        R.verify_json_key_for_not_null(response.json()["bookingid"])

    @pytest.mark.negative
    @allure.title("Verify that Create Booking doesn't work with no payload")
    @allure.description(
        "Creating a Booking with no payload and verify that booking id")
    def test_create_booking_negative(self):
        response = Crud_operation.post_request(url=R.create_booking_url(),auth=None,headers=R.common_headers_json(),
                                               payload={},in_json=False)
        R.verify_http_status_code(response_data=response, expect_data=200)
        R.verify_json_key_for_not_null(response.json()["bookingid"])
        response = Crud_operation.post_request(url=R.create_booking_url(),auth=None,
                                               headers=R.common_headers_json(),payload={},in_json=False)
        R.verify_http_status_code(response_data=response, expect_data=500)





