import requests
import json



class Url:

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def create_booking_url():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def create_token_url():
        return "https://restful-booker.herokuapp.com/auth"

    # Update, PUT, PATCH, DELETE - bookingId
    def patch_put_delete_url(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)


class Crud_operation(Url):

    @staticmethod
    def get_request(url, auth):
        response = requests.get(url=url, auth=auth)
        return response.json()

    @staticmethod
    def post_request(url, auth, headers, payload, in_json):
        post_response = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
        if in_json is True:
            return post_response.json()
        return post_response

    @staticmethod
    def patch_requests(url, headers, auth, payload, in_json):
        patch_response_data = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
        if in_json is True:
            return patch_response_data.json()
        return patch_response_data

    @staticmethod
    def put_requests(url, headers, auth, payload, in_json):
        put_response_data = requests.put(url=url, headers=headers, auth=auth, data=json.dumps(payload))
        if in_json is True:
            return put_response_data.json()
        return put_response_data

    @staticmethod
    def delete_requests(url, headers, auth, in_json):
        delete_response_data = requests.delete(url=url, headers=headers, auth=auth)
        if in_json is True:
            return delete_response_data.json()
        return delete_response_data

class Payload(Crud_operation):

    @staticmethod
    def create_booking_payload():
        payload = {
            "firstname": "Amit",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        return payload

    @staticmethod
    def create_token_payload():
        payload = {
            "username": "admin",
            "password": "password123"
        }
        return payload

class Headers(Payload):

    @staticmethod
    def common_headers_json():
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    @staticmethod
    def common_headers_xml():
        headers = {
            "Content-Type": "application/xml",
        }
        return headers

    @staticmethod
    def common_header_put_patch_delete_basic_auth(basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic " + str(basic_auth_value),
        }
        return headers

    @staticmethod
    def common_header_put_delete_patch_cookie(token):
        headers = {
            "Content-Type": "application/json",
            "Cookie": "token=" + str(token),
        }
        return headers

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database(self):
        pass

class Verification(Headers):
    @staticmethod
    def verify_http_status_code(response_data, expect_data):
        assert response_data.status_code == expect_data, "Failed ER!=AR"

    @staticmethod
    def verify_response_key(key, expected_data):
        assert key == expected_data

    @staticmethod
    def verify_json_key_for_not_null(key):
        assert key != 0, "Failed - Key is non Empty" + key
        assert key > 0, "Failed - Key is grater than zero"

    @staticmethod
    def verify_json_key_for_not_null_token(key):
        assert key != 0, "Failed - Key is non Empty" + key

    @staticmethod
    def verify_response_key_should_not_be_none(key):
        assert key is not None

    @staticmethod
    def verify_response_delete(response):
        assert "Created" in response

class R(Verification):
    pass