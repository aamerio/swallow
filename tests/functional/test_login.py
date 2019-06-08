# coding=utf-8
"""Login feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from api.login import *

@scenario('../../features/login.feature', 'Login validation')

@given('valid_token')
def valid_token():
    """Login validation."""
    registry = SingleSignOnRegistry()
    token = registry.register("valid credentials")
    login = Login(registry)

    response = login.handle_request("do stuff", token)
    assert "hello world" in response

def test_invalid_token():
    registry = SingleSignOnRegistry()
    my_service = Login(registry)

    response = my_service.handle_request("do stuff", token=None)
    assert "please enter your login details" in response
