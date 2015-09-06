# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache
from sqlalchemy.orm.exc import NoResultFound
import uuid
import re
from time import time
import json
class RegisterHandler(BaseHandler):
    def get(self):
        if not self.current_user:  
            self.render('login.html')  
        else:  
            self.redirect('/') 
    def post(self):
        arg_name=self.get_argument("name")
        arg_password=self.get_argument("password")
        arg_uid=self.get_argument('uid')
        retjson = {'code':200,'content':'ok','uid' : 'null'}
        if not arg_password or not arg_name or not arg_uid:
            retjson['code'] = 400
            retjson['content'] = u'Arguments is empty~'
        elif len(arg_password) < 6 :
            retjson['code'] = 403
            retjson['content'] = u'Your password is too short'
        else:
            try:
                #user has exit?
                self.db.query(UsersCache).filter(UsersCache.uid==arg_uid).update({UsersCache.name:arg_name,UsersCache.password : arg_password})
               
                cookie_uuid=uuid.uuid1()
                self.set_secure_cookie("username",str(cookie_uuid),expires_days=30,expires=int(time())+2592000)
                status_cookie = CookieCache(cookie=cookie_uuid,uid=arg_uid)
                try:
                    self.db.commit()
                except Exception, e:
                    print '11111111111'
                    raise self.db.rollback()
                    retjson['code'] = 401
                    retjson['content'] = u'Database store is wrong!'
            except NoResultFound:
                retjson['code'] = 402
                retjson['content'] = "Sql store is wrong!Try again!"
        ret = json.dumps(retjson,ensure_ascii=False, indent=2)
        self.write(ret)


class VerifyHandler(BaseHandler):
    def post(self):
        retjson = {'code':200,'content':'ok'}
        arg_info_email=self.get_argument('info_email')
        arg_student_card=self.get_argument('student_card')
        arg_student_id = self.get_argument('student_id')
        if not arg_info_email or not arg_student_id or not arg_student_card :
            retjson['code'] = 400
            retjson['content'] = u'Arguments is empty~'
        elif re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", arg_info_email) == None :
            retjson['code'] = 404
            retjson['content'] = u'Your email format is wrong'
        else :
            try:
                person = self.db.query(UsersCache).filter(UsersCache.student_card==arg_student_card).one()
                retjson['code'] = 401
                retjson['content'] = u'user %s has exited!' % (person.student_card)
            except NoResultFound :
                uid_uuid = uuid.uuid5(uuid.NAMESPACE_DNS,str(arg_info_email))
                status_users = UsersCache(student_card = arg_student_card,student_id = arg_student_id,uid = uid_uuid,info_email = arg_info_email)
                self.db.add(status_users)
                try:
                    self.db.commit()
                    retjson['content'] = {'uid':str(uid_uuid),'content':'Verify pass!'}
                except Exception, e:
                    raise self.db.rollback()
                    retjson['code'] = 401
                    retjson['content'] = u'Database store is wrong!'
        ret = json.dumps(retjson,ensure_ascii=False, indent=2)
        self.write(ret)
