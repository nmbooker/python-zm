#! /usr/bin/env python

"""Contact manager.
"""

import zm.contacts
import zm.restauth

class ContactsDownloadManager(object):
    def __init__(self, view):
        self.view = view

    def download(self):
        homeurl = self.view.get_homeurl()
        credentials = self.view.get_login_info()
        login_key = zm.restauth.LoginKey(**credentials)
        fmt_options = self.view.get_format_options()
        contacts_srv = zm.contacts.ZimbraContacts(
                homeurl=homeurl, login_key=login_key)
        try:
            result = contacts_srv.download(**fmt_options)
        except urllib2.HTTPError, exc:
            self.view.handle_http_error(code=exc.code)
            return
        self.view.save_contacts_download(result)
