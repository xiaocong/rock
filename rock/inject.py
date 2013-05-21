# -*- coding: utf-8 -*-

import functools
import inspect
from .ps import emit

__all__ = ["pub_message", "device_attr", "pub_result"]


def _pub_message_around_method(method):
    ''' Publish message before and after "setUp", "tearDown", "test...."
        method is invoked.
    '''
    if method.__name__ == "setUp":
        topic = "test.setup"
    elif method.__name__ == "tearDown":
        topic = "test.teardown"
    elif method.__name__.startswith("test"):
        topic = "test.testing"
    else:
        topic = None

    @functools.wraps(method)
    def wrapped(self, *args, **kwargs):
        emit(topic, data={"when": "before", "id": self.id()})
        try:
            method(self, *args, **kwargs)
        except:
            raise
        finally:
            emit(topic, data={"when": "after", "id": self.id()})

    return topic and wrapped or method


def pub_message(cls):
    ''' Inject message publishing for methods of the cls
    '''
    for name, method in inspect.getmembers(cls, predicate=inspect.ismethod):
        if name == "setUp" or name == "tearDown" or name.startswith("test"):
            setattr(cls, name, _pub_message_around_method(method))
    return cls


def device_attr(attribute_name, device_impl):
    ''' Inject device attribute to the class
    '''
    def wrapped(cls):
        setattr(cls, attribute_name, device_impl())
        return cls

    return wrapped


def pub_result(cls):
    ''' Inject message publishing for test case result
    '''
    original_run = cls.run

    def run(self, result=None):
        if result is None:
            original_run(self, result)
        else:
            e, f, t = len(result.errors), len(result.failures), result.testsRun
            original_run(self, result)
            ne, nf, nt = len(result.errors), len(result.failures), result.testsRun
            if nf - f == 1:
                emit("test.result", data={"result": "failure", "id": self.id()})
            elif ne - e == 1:
                emit("test.result", data={"result": "error", "id": self.id()})
            elif nt - t == 1:
                emit("test.result", data={"result": "pass", "id": self.id()})

    setattr(cls, "run", run)
    return cls
