import inspect
import pytest
import requests
import json
from random_date_for_request import get_random_parametrize_for_request


@pytest.mark.parametrize("random_data_for_request", get_random_parametrize_for_request(division_type_operation=False))
def test_rout_multiplication_numbers(random_data_for_request: dict, rout_multiplication: str, get_date_time: str):
    """Тестирование функции умножения"""
    data = random_data_for_request.copy()
    expect_status_code = data.pop("statusCode")  # pop а не get дабы исключить лишние ключи для метода post
    expect_status_message = data.get("statusMessage", None)
    if expect_status_message:
        data.pop("statusMessage")  # pop а не get дабы исключить лишние ключи для метода post
    expect_result = None
    x = data.get("x", None)
    y = data.get("y", None)
    if isinstance(x, int) and isinstance(y, int):
        expect_result = x * y
    with requests.post(rout_multiplication, data=json.dumps(data)) as response:
        result = response.json()
        response_status_code = result.get("statusCode", None)
        response_result = result.get("result", None)
        response_status_message = result.get("statusMessage", None)
    report_string = f"ERROR {inspect.currentframe().f_code.co_name} ->> {get_date_time} {response_status_code=} {expect_status_code=} {x=} {y=} {response_result=} {expect_result=} {response_status_message=} {expect_status_message=}"
    if response_result:
        assert response_result == expect_result, report_string
    if response_status_code:
        assert response_status_code == expect_status_code, report_string
    if response_status_code != 0:
        assert response_status_message == expect_status_message, report_string
