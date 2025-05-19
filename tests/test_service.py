import requests

import unittest.mock as mock
import source.service as service
import pytest

@mock.patch('source.service.get_user_from_db')
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user = service.get_user_from_db(1)
    assert user == "Mocked Alice"
    mock_get_user_from_db.assert_called_once_with(1)

@mock.patch('requests.get')
def test_get_user_from_service(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"id": 1, "name": "Alice"}]
    
    users = service.get_users()
    assert len(users) == 1
    assert users[0]['name'] == "Alice"
    mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users")

@mock.patch('requests.get')
def test_get_user_from_service_2(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "Alice"}]
    mock_get.return_value = mock_response
    
    users = service.get_users()
    assert len(users) == 1
    assert users[0]['name'] == "Alice"
    mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users")

@mock.patch('requests.get')
def test_get_user_from_service_failure(mock_get):   
    mock_get.return_value.status_code = 404
    with pytest.raises(requests.HTTPError):
        service.get_users()