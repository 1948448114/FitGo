# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache
class LoginHandler(BaseHandler):
    @property
    def db(self):
        return self.application.db
    def on_finish(self):
        self.db.close()

    def get(self):
        self.render('login.html')

    def post(self):
        info_email=self.get_argument("info_email")
        user_password=self.get_argument("user_password")
        code=self.get_argument("code")
        if info_email=="" or user_password=="" or code=="" :
            self.write("{'code':{400},'content':'Empty'}")
        else:
            try:
                person=self.db.query(UsersCache).filter(UsersCache.info_email==info_email,UsersCache.password == user_password).one()
                self.set_secure_cookie("username", self.get_argument("info_email"),expires_days=30,expires=time.time()+2592000)
                self.write("{'code':{200},'content':'ok'}")
            except Exception, e:
                print e
                self.write("{'code':{400},'content':'not found'}")
        # if 1 :
        #     self.set_secure_cookie("username", self.get_argument("info_email"))
        #     self.write("{'code':{200},'content':'ok'}")
        #     self.finish()
        #     self.redirect("/")

class LogoutHandler(BaseHandler):
    def get(self):
        if (self.get_argument("logout", None)):
            self.clear_cookie("username")
            self.redirect("/")
