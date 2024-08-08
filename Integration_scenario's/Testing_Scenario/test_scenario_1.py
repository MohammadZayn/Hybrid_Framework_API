import pytest
import requests
import allure


@allure.title("#Test_Case -1")
@allure.description("Verify that Create Booking -> Patch Request - Verify that firstName is updated.")
@allure.tag("Integration", "#1", "TestCase")
@allure.label("Owner", "Mohammad_Zain")
@allure.testcase("Integration_Testing_1")
def test_patch_booking(Patch_Booking):
    data = Patch_Booking
    assert "firstname" in Patch_Booking
    assert Patch_Booking["firstname"] == "Jane"
    print(data)