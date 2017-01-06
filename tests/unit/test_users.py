# encoding: utf-8
# pytest-bdd generate users.feature > test_users.py
# http://pydigger.com/pypi/pytest-bdd
"""User feature tests."""

import pytest
from pytest_bdd import (scenario, given, when, then)

from api.user import User


@pytest.fixture
def user():
    user = User({'token': 'some-awesome-apikey', 'env': 'test', 'user': 'admin'})
    return user


@scenario('../../features/user.feature', 'Reclaim the user')
def test_reclaim_the_users_list():
    """Reclaim the users list."""
    pass


@given('The auth dict is valid')
def test_auth_is_valid(user):
    assert user.auth_is_valid() == True


@given('The user has a token')
def test_user_has_token(user):
    """I have an environment."""
    assert user.auth['token'] != ''


@given('The user has an environment')
def test_user_has_env(user):
    """I have an environment."""
    assert user.auth['env'] != ''


@then('The list is pushed')
def test_users_list_accessible(user):
    """Return the list."""
    assert user.users() != {}


@then('User details are pushed')
def test_user_details_are_pushed(user):
    """Return the list"""
    assert user.info() != {}
