import pytest
from main import get_weather

def test_getGoRestApu(mocker):

    mock_get=mocker.patch("main.requests.get")

    # Set return values
    mock_get.return_value.status_code=200
    mock_get.return_value.json.return_value={"age": "Karan Sethi", "emaifdgfdgfdgl": "karan_sethi@langworth-yundt.test"}

    #Call the function
    result=get_weather()


    #Assertions
    assert result=={"age": "Karan Sethi", "emaifdgfdgfdgl": "karan_sethi@langworth-yundt.test"}
    mock_get.assert_called_once_with("https://gorest.co.in/public/v2/users/")

