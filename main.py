# -*- coding: utf-8 -*-
#!/usr/bin/env python
#@date  :2015-3-from
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
from tornado.options import define, options
from UI_moudles.UI_moudle import *

define("port", default=8888, help="run on the given port", type=int)


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        info_email=self.get_argument("info_email")
        user_password=self.get_argument("user_password")
        code=self.get_argument("code")
        if 1 :    
            self.set_secure_cookie("username", self.get_argument("info_email"))
            self.write("{'code':{200},'content':'ok'}")
            # self.finish()
            # self.redirect("/")

class WelcomeHandler(BaseHandler):
    # @tornado.web.authenticated
   
    def get(self):
        # if not self.current_user:
        #     print " no user redirect to login "
        #     self.redirect("/auth/login")
        # return
        self.render('index.html', user=self.current_user)

class LogoutHandler(BaseHandler):
    def get(self):
        if (self.get_argument("logout", None)):
            self.clear_cookie("username")
            self.redirect("/")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',WelcomeHandler),
            (r'/body',BodyHandler),
            (r'/auth/login',LoginHandler),
            (r'/auth/logout', LogoutHandler)
            ]
        settings = dict(
            cookie_secret="<7CA71A57B571B5AEAC5E64C6042415DE></7CA71A57B571B5AEAC5E64C6042415DE>",
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            ui_modules={'header':HeaderMoudle,'footer':FooterMoudle},
            # xsrf_cookies=True,
            login_url="/auth/login",
            # static_url_prefix = os.path.join(os.path.dirname(__file__), '/images/'),
            debug=True,
            # "lohin_url":"/auth/LoginHandler"
            
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('body.html')

class BodyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('body.html')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
