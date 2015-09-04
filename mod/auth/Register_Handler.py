# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache
from sqlalchemy.orm.exc import NoResultFound
import uuid
from time import time
import json
class RegisterHandler(BaseHandler):
    def get(self):
        if not self.current_user:  
            self.render('login.html')  
        else:  
            self.redirect('/') 
    def post(self):
        aname=self.get_argument("name")
        astudent_card=self.get_argument("student_card")
        astudent_id=self.get_argument("student_id")
        ausername=self.get_argument("username")
        apassword=self.get_argument("password")
        ainfo_email=self.get_argument("info_email")
        retjson = {'code':200,'content':'ok'}
        if not aname or not astudent_card or not astudent_id or not ausername or not apassword or not ainfo_email :
            retjson['code'] = 400
            retjson['content'] = u'参数不能为空哦~'
        else:
            try:
                #user has exit?
                person = self.db.query(UsersCache).filter(UsersCache.info_email==ainfo_email).one()
                retjson['code'] = 401
                retjson['content'] = u'user has exited!'
            except NoResultFound:
                cookie_uuid=uuid.uuid1()
                uid_uuid = uuid.uuid5(uuid.NAMESPACE_DNS,str(ainfo_email))

                self.set_secure_cookie("username",str(cookie_uuid),expires_days=30,expires=int(time())+86400)
                status_cookie = CookieCache(cookie=cookie_uuid,uid=uid_uuid)
                status_users = UsersCache(uid=uid_uuid,name=aname,student_id=astudent_id,student_card=astudent_card,user_name=ausername,password=apassword,info_email=ainfo_email)
                self.db.add(status_cookie)
                self.db.add(status_users)
                try:
                    self.db.commit()
                except:
                    self.sb.rollback()
                    retjson['code'] = 402
                    retjson['content'] = "Sql store is wrong!Try again!"
        ret = json.dumps(retjson,ensure_ascii=False, indent=2)
        self.write(ret)
