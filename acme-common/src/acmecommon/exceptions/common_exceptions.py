# -*- coding: utf-8 -*-


class NotSupportedException(Exception):
    def __init__(self, message, errors):
        super(__class__, self).__init__(message)
        self.errors = errors


class CustomException(Exception):
    pass


def raise_custom_exception():
    raise CustomException("Test to raise custom exception")
