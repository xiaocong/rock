# -*- coding: utf-8 -*-

from pubsub import pub


def emit(topic, *args, **kwargs):
    pub.sendMessage(topic, *args, **kwargs)


def on(topic, func):
    pub.subscribe(func, topic)
