from shopping import query_pchome
from shopping import valid_password
import json
import sys

from unittest import mock
from fastapi.testclient import TestClient

from .main import app

sys.path.append(".")

client = TestClient(app)

def test_valid_password():
    with mock.patch(
        "shopping.time.sleep",
        side_effect=[None]
    ) as sleep:
        assert valid_password(10) is False
    sleep.assert_called_once_with(10)

def test_jon():
    import json 

    with open("./pchome_battery.json", encoding="utf-8") as f:
        data = json.loads(f.read())

    assert data["Prods"][0]["Name"] == "超強行動電源"


# def test_query_pchome_will_return_list_of_pricing_and_name():

#     with open("./pchome_battery.json", encoding="utf-8") as f:
#         data = json.loads(f.read())

#     def mock_get(url, *args, **kwargs):
#         response = mock.Mock()
#         response.json.return_value = data
#         return response 

#     with mock.patch("shpping.requests.get") as get:
#         get.side_effect = mock_get
#         result = query_pchome("行動電源")

#     # result = query_pchome("行動電源")

#     assert len(result) > 0
#     assert "pricing" in result[0]
#     assert isinstance(result[0]["pricing"], float)

#     assert "name" in result[0]
#     assert isinstance(result[0]["name"], str)

def test_pricing_will_return_200_with_keyword():
    response = client.get("/pricing?keyword=行動電源")
    assert response.status_code == 200
    assert len(response.json()) > 0
    data = response.json()
    assert "name" in data[0]
    assert "pricing" in data[0]

    assert isinstance(data[0]["name"], str)
    assert isinstance(data[0]["pricing"], float)

