# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
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