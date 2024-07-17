from datetime import datetime
from pytest import fixture

URL_BASE = "http://localhost:12000/api/"


@fixture
def get_date_time():
    yield datetime.now().strftime("%d/%m/%Y | %H:%M:%S")


@fixture
def rout_addition():
    addition_url = f"{URL_BASE}addition"
    yield addition_url


@fixture
def rout_division():
    division_url = f"{URL_BASE}division"
    yield division_url


@fixture
def rout_multiplication():
    multiplication_url = f"{URL_BASE}multiplication"
    yield multiplication_url


@fixture
def rout_remainder():
    remainder_url = f"{URL_BASE}remainder"
    yield remainder_url


@fixture
def rout_state():
    state_url = f"{URL_BASE}state"
    yield state_url
