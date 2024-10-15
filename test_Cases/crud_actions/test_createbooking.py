import allure
import pytest
from Source_Content.Common_Passers import *

class Test_Create_Booking:
    @allure.title("#Test_Case -3")
    @allure.description("Verify that Create Booking -> Patch Request - Verify that firstName is updated.")
    @allure.tag("Integration", "#3", "TestCase")
    @allure.label("Owner", "Mohammad_Zain")
    @allure.testcase("Integration_Testing_3")
    def test_create_booking(self):
        print("Create Booking Testcase")
        response = Crud_operation.post_request(url=R.create_booking_url(),auth=None,headers=R.common_headers_json(),
                                               payload=R.create_booking_payload(), in_json=False)
        R.verify_http_status_code(response_data=response, expect_data=200)
        R.verify_json_key_for_not_null(response.json()["bookingid"])





