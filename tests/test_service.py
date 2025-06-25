import pytest
from service import  UserService ,APIClient

def test_service(mocker):
   # Create a mock api client
    mock_api_client=mocker.Mock(spec=APIClient)

   #Mock get_user_data to return a fake user
    mock_api_client.get_user_data.return_value={"id" :1,"name":"Vanita"}
    service=UserService(mock_api_client)
    result=service.get_username(1)
    print("RESULT---" +result)

   # Assertions
   assert result=="VANITA"  #Check if processing was done correctly
   mock_api_client.get_user_data.assert_called_once_with(1)  #Ensure correct API call


