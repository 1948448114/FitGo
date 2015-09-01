# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
from tornado.options import define, options
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
        self.render('header.html')

class BodyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('body.html')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
