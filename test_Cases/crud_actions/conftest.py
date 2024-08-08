import pytest
from Source_Content.Common_Passers import R


@pytest.fixture(scope="session")
def create_token():
    response = R.post_request(url=R.create_token_url(), headers=R.common_headers_json(), auth=None,
                              payload=R.create_token_payload(), in_json=False)
    R.verify_http_status_code(response_data=response, expect_data=200)
    R.verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]

@pytest.fixture(scope="session")
def get_booking_id():
    response = R.post_request(url=R.create_booking_url(), auth=None,
                              headers=R.common_headers_json(), payload=R.create_booking_payload(), in_json=False)
    booking_id = response.json()["bookingid"]
    R.verify_http_status_code(response_data=response, expect_data=200)
    R.verify_json_key_for_not_null(booking_id)
    return booking_id
