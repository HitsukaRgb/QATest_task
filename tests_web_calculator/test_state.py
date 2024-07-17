import requests


def test_state(rout_state: str):
    """Тестирование функции получения статуса сервера"""
    with requests.get(rout_state) as response:
        result = response.json()
        assert result == {'statusCode': 0, 'state': 'OК'}
