# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache
import json
from time import time
import uuid
class LoginHandler(BaseHandler):
    def get(self):
        if not self.current_user:  
            self.render('login.html')  
        else:  
            self.redirect('/')  
        

    def post(self):
        info_email=self.get_argument("info_email")
        user_password=self.get_argument("user_password")
        code=self.get_argument("code")
        retjson = {'code':200,'content':'ok'}
        if not info_email or not user_password or not code :
            retjson['code'] = 400
            retjson['content'] = u'参数不能为空哦~'
        else:
            try:
                #user is right?
                person=self.db.query(UsersCache).filter(UsersCache.info_email==info_email,UsersCache.password == user_password).one()
                #yes => set cookie
                cookie_uuid=uuid.uuid1()
                self.set_secure_cookie("username",str(cookie_uuid),expires_days=30,expires=int(time())+86400)
                #ok => store
                status = CookieCache(cookie=cookie_uuid,uid=person.uid)
                self.db.add(status)
                try:
                    self.db.commit()
                except:
                    self.sb.rollback()
                ret=json.dumps({'code':200,'content':'ok'},ensure_ascii=False,indent=2)
                self.write(ret)
            except Exception, e:
                print e
                retjson['code'] = 400
                retjson['code'] = u'用户名或者密码错误'
        ret = json.dumps(retjson,ensure_ascii=False, indent=2)
        self.write(ret)

class LogoutHandler(BaseHandler):
    def get(self):
        if (self.get_argument("logout", None)):
            self.clear_cookie("username")
            self.redirect("/")
