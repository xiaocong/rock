# -*- coding: utf-8 -*-

from .device import BaseDevice
from .inject import pub_message, pub_result, device_attr
from fn import F

__all__ = ["Android"]


class AndroidImpl(BaseDevice):
    ''' The implementation of Android device
    '''
    pass


Android = F() << pub_result << pub_message << device_attr("d", AndroidImpl)
