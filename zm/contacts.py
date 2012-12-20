#! /usr/bin/env python

import urllib2
import sys
import restauth

class ZimbraContacts(object):
    """Zimbra's Contacts System"""
    def __init__(self, homeurl, login_key):
        self.homeurl = homeurl
        self.login_key = login_key


    def download(self, fmt='csv', csvfmt=None):
        """Download the contact details.
        Returns a file-like response object.
        """
        request = self._request(fmt=fmt, csvfmt=csvfmt)
        return urllib2.urlopen(request)
        

    def _request(self, fmt, csvfmt=None):
        url = self._url(fmt=fmt, csvfmt=csvfmt)
        request = urllib2.Request(url)
        if self.login_key:
            self.login_key.basic_authenticate(request)
        return request

    def _url(self, fmt, csvfmt=None):
        url = self.homeurl
        url += ("/contacts?%s&fmt=%s" % (self.login_key.auth_url_param(), fmt))
        if csvfmt is not None:
            url += ("&csvfmt=%s" % (csvfmt))
        return url
