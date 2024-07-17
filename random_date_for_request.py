import random

"""Статические положительные/отрицательные тесты"""
_static_parametrize_list = [
    {"x": "some_x_numer", "y": 12, "statusMessage": "Значения параметров должны быть целыми", "statusCode": 3},
    {"x": 12, "y": "some_y_numer", "statusMessage": "Значения параметров должны быть целыми", "statusCode": 3},
    {"x": 12, "y": 0.25, "statusMessage": "Значения параметров должны быть целыми", "statusCode": 3},
    {"x": 0.25, "y": 12, "statusMessage": "Значения параметров должны быть целыми", "statusCode": 3},
    {"x": "some_x_numer", "y": "some_y_numer", "statusMessage": "Значения параметров должны быть целыми",
     "statusCode": 3},
    {"x": 0, "y": 12, "statusMessage": "Все хорошо", "statusCode": 0},
    {"x": -2147483648, "y": 2147483647, "statusMessage": "Все хорошо", "statusCode": 0},
    {"x": -2147483649, "y": 2147483648, "statusMessage": "Превышены максимальные значения параметров", "statusCode": 4},
    {"x": -2147483649, "y": 2147483647, "statusMessage": "Превышены максимальные значения параметров", "statusCode": 4},
    {"x": -2147483648, "y": 2147483648, "statusMessage": "Превышены максимальные значения параметров", "statusCode": 4},
    {"y": 12, "statusMessage": "Не указаны необходимые параметры", "statusCode": 2},
    {"x": 12, "statusMessage": "Не указаны необходимые параметры", "statusCode": 2},
]


def _random_parametrize_list() -> list[dict[str, int]]:
    """Генерация рандомных положительных тестов"""
    random_parametrize_list = []
    for _ in range(15):
        x, y = random.randint(-2147483648, 2147483647), random.randint(-2147483648, 2147483647)
        random_parametrize_list.append({"x": x, "y": y, "statusCode": 0})
    return random_parametrize_list


def get_random_parametrize_for_request(division_type_operation: bool = False) -> list[dict[str, int]]:
    """Функция получения набора данных для тестирования"""
    result = _static_parametrize_list + _random_parametrize_list()
    return result if not division_type_operation else result + [{"x": 12, "y": 0, "statusMessage": "Ошибка вычисления", "statusCode": 1}]
