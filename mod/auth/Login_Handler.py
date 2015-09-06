# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache
import json
from time import time
import uuid
import re
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
        is_remember = self.get_argument('is_remember')
        retjson = {'code':200,'content':'ok'}
        if not info_email or not user_password :
            retjson['code'] = 400
            retjson['content'] = u'Arguments are empty'
        else:
            try:
                #user is right?
                person=self.db.query(UsersCache).filter(UsersCache.info_email==info_email,UsersCache.password==user_password).one()
                #yes => set cookie
                cookie_uuid=uuid.uuid1()
                if is_remember :
                    self.set_secure_cookie("username",str(cookie_uuid),expires_days=30,expires=int(time())+2592000)
                else:
                    self.set_secure_cookie('username',str(cookie_uuid),expires_days=None)
                #ok => store
                status = CookieCache(cookie=cookie_uuid,uid=person.uid)
                self.db.add(status)
                try:
                    self.db.commit()
                except:
                    self.sb.rollback()
                    retjson['code'] = 401
                    retjson['content'] = u'Database store is wrong!'
            except Exception, e:
                print e
                retjson['code'] = 402
                retjson['content'] = u'User name or password is wrong!'
        ret = json.dumps(retjson,ensure_ascii=False, indent=2)
        print ret
        self.write(ret)

