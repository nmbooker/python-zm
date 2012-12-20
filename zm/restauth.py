#! /usr/bin/env python

"""Zimbra REST interface authentication"""

import base64

class LoginKey(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def basic_authenticate(self, request):
        """Add basic authentication header to urllib2.Request object."""
        basic_authenticate(request, self.username, self.password)
        
    def auth_url_param(self):
        return "auth=ba"


def basic_authenticate(request, username, password):
    """Add basic authentication header to Request object.

    request: A urllib2.Request object.
    username: Username to log in with.
    password: Password to log in with.

    No return value.  request is modified in-place.
    """
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header('Authorization', ('Basic %s' % base64string))
 
