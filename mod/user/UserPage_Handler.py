# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
import tornado.web
import tornado.gen
import json
import uuid
import re
from time import time

from ..databases.tables import TopicsCache
from ..databases.tables import UsersCache 
from ..databases.tables import User_tagCache

from Base_Handler import BaseHandler


class UserPageHandler(BaseHandler):
    """docstring for WatchUser_handler"""

    @property
    def db(self):
        return self.application.db


    def on_finish(self):
        self.db.close()

    def get(self,user_id):
        self.render("infochange.html",user = self.current_user)



    def post(self,user_id):
        # 获取id
        # uid = self.get_argument('id')

        retjson = {'code':200,'content':'ok'}

        uid = user_id


        gender = self.get_argument('gender') 
        user_name = self.get_argument('user_name') 
        school = self.get_argument('school') 
        campus = self.get_argument('campus') 

        info_email = self.get_argument('info_email') 
        info_phone = self.get_argument('info_phone') 
        portrait = self.get_argument('portrait') 

        # self.write(campus+info_email+info_phone+portrait+user_name)

        if not gender or not user_name or not school or not campus or not info_email or not info_phone or not portrait:
            retjson['code'] = 400
            retjson['content'] = u'Arguments is empty'
        	# retjson['code'] = 400
            # retjson['content'] = u'Arguments is empty'
            


        elif re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", info_email) == None :
            retjson['code'] = 404
            retjson['content'] = u'Your email format is wrong'


        else:
            try:
                # get the DBinfo of the person UID equals uid
                t1 = self.db.query(UsersCache).filter(UsersCache.uid == uid)
                # update the data of personal infomation 
                t1.update({UsersCache.gender:gender,UsersCache.user_name:user_name,UsersCache.school:school,UsersCache.campus:campus,UsersCache.info_email:info_email,UsersCache.info_phone:info_phone,UsersCache.portrait:portrait})
               
                try:
                    self.db.commit()
                    
                except Exception, e:
                    self.db.rollback()
                    retjson['code'] = 401
                    retjson['content'] = u'Database store is wrong!'


            except Exception, e:
                retjson['code'] = 402
                retjson['content'] = "Sql store is wrong!Try again!"

        #format json
        ret = json.dumps(retjson,ensure_ascii=False, indent=2)
        self.write(ret)



        
