import allure

@allure.title("#Test_Case -6")
@allure.description("Trying to Update on a Delete ID -> 404")
@allure.tag("Integration", "#6", "TestCase")
@allure.label("Owner", "Mohammad_Zain")
@allure.testcase("Integration_Testing_6")
def test_Try_To_Update_A_Deleted_ID(Delete_Booking, Put_Booking):
    booking_id = Delete_Booking
    print(booking_id)
    baseurl = "https://restful-booker.herokuapp.com/booking/" + booking_id
    
    try:
       response = Put_Booking(baseurl)
       response.raise_for_status()
       print(f"Booking details: {response.json()}")
        
       var = response.status_code == 200, "Please check the booking id it is not exists in database"
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Error: Booking ID {invalid_booking_id} not found. (HTTP 404)")
        else:
            print(f"HTTP error occurred: {http_err}")
            
    except Exception as err:
        print(f"An error occurred: {err}")

