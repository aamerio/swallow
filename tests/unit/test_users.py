# coding=utf-8
# pytest-bdd generate users.feature > test_users.py

"""Users feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
import pytest

@pytest.fixture
def admin():
    """Admin fixture."""
    auth = {'token':'some-awesome-apikey', 'env': 'test', 'user': 'admin'}
    return auth

@scenario('users.feature', 'Reclaim the users list')
def test_reclaim_the_users_list():
    """Reclaim the users list."""
    pass


@given('I have an environment')
def i_have_an_environment(admin):
    """I have an environment."""
    assert admin['env'], 'test'


@given('I\'m an authorized user')
def im_an_authorized_user():
    """I'm an authorized user."""
    pass


@when('I go to the users list page')
def i_go_to_the_users_list_page():
    """I go to the users list page."""
    pass


@then('I should not see the error message')
def i_should_not_see_the_error_message():
    """I should not see the error message."""
    pass


@then('the list is pushed')
def the_list_is_pushed():
    """the list is pushed."""

