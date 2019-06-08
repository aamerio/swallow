# encoding: utf-8


class User(object):

    def __init__(self, auth):
        self.empty_auth = {'token': '', 'env': '', 'user': ''}
        self.auth = auth
        self.details = {}

    def auth_is_valid(self):
        if sorted(self.auth.keys()) != sorted(self.empty_auth.keys()) \
                or "".join(self.auth.keys()) == "":
            return False
        return True

    def users(self):
        if self.auth_is_valid():
            return {'users': {}}
        return {}

    def info(self):
        if self.auth_is_valid():
            return {'info': {}}
        return {}

