# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

