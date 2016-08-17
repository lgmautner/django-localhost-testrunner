# -*- coding: utf-8 -*-

import sys
import copy
from urlparse import urlparse
from unittest import TextTestRunner
import socket

LOCAL_HOSTNAMES = [
    'localhost',
    '127.0.0.1',
]

create_connection = copy.deepcopy(socket.create_connection)
getaddrinfo = copy.deepcopy(socket.getaddrinfo)

ERROR_MSG = "{} is a non-local URL"

def socket_create_connection(address, **kwargs):
    assert urlparse(address).hostname in LOCAL_HOSTNAMES, ERROR_MSG.format(address)
    return create_connection(address, **kwargs)

def socket_getaddrinfo(host, *args, **kwargs):
    assert host in LOCAL_HOSTNAMES, ERROR_MSG.format(host)
    return getaddrinfo(host, *args, **kwargs)

class LocalhostTestRunner(TextTestRunner):
    def __init__(self, stream=sys.stderr, descriptions=True, verbosity=1,
                 failfast=False, buffer=False):
        # monkeypatch socket
        socket.create_connection = socket_create_connection
        socket.getaddrinfo = socket_getaddrinfo
        TextTestRunner.__init__(self, stream, descriptions, verbosity,
                                failfast=failfast, buffer=buffer)
