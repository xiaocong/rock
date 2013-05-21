# -*- coding: utf-8 -*-


class BaseDevice(object):

    def __init__(self):
        pass

    def __get__(self, obj, type=None):
        return obj and self.__class__() or self

    def __call__(self):
        return self
