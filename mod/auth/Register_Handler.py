# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache
from sqlalchemy.orm.exc import NoResultFound


#name;student_card;student_id;username;password;info_email；
class RegisterHandler(BaseHandler):
    def get(self):
        if not self.current_user:  
            self.render('login.html')  
        else:  
            self.redirect('/') 
    def post(self):
        name=self.get_argument("name")
        student_card=self.get_argument("student_card")
        student_id=self.get_argument("student_id")
        username=self.get_argument("username")
        password=self.get_argument("password")
        info_email=self.get_argument("info_email")
        retjson = {'code':200,'content':'ok'}
        if not name or not student_card or not student_id or not username or not password or not info_email :
            retjson['code'] = 400
            retjson['content'] = u'参数不能为空哦~'
        else:
            try:
                #user has exit?
                person = self.db.query(UsersCache).filter(UsersCache.info_email==info_email).one()
                retjson[code] = 401
                retjson[content] = u'user has exited!'
            except NoResultFound:
                cookie_uuid=uuid.uuid1()
                self.set_secure_cookie("username",str(cookie_uuid),expires_days=30,expires=int(time())+86400)
                status = CookieCache(cookie=cookie_uuid,uid=person.uid)
                self.db.add(status)
                try:
                    self.db.commit()
                except:
                    self.sb.rollback()
        ret = json.dumps(retjson,ensure_ascii=False, indent=2)
        self.write(ret)
