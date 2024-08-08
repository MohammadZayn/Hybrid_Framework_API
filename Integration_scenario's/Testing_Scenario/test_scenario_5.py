import allure

@allure.title("#Test_Case -5")
@allure.description("Invalid Creation - enter a wrong payload or Wrong JSON.")
@allure.tag("Integration", "#5", "TestCase")
@allure.label("Owner", "Mohammad_Zain")
@allure.testcase("Integration_Testing_5")
def test_Invalid_Payload(Create_Booking_With_Invalid_Payload):
    response = Create_Booking_With_Invalid_Payload
    assert response.status_code == 200, "Given payload have an issue please check and correct"