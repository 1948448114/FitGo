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

from ..auth.Base_Handler import BaseHandler



class UserPageHandler(BaseHandler):
    """修改个人信息"""
    def get(self,user_id):
        self.render("infochange.html",user = self.current_user)

    def post(self,user_id):
        # 获取id
        # uid = self.get_argument('id')
        retjson = {'code':200,'content':'ok'}
        uid = user_id
        try:
            gender = self.get_argument('gender') 
            name = self.get_argument('name') 
            school = self.get_argument('school') 
            campus = self.get_argument('campus') 
            tag = self.get_argument('tag') 
            info_phone = self.get_argument('info_phone') 
            signature = self.get_argument('signature') 
            # self.write(campus+info_email+info_phone+portrait+user_name)

            if not gender or not name or not school or not campus or not info_phone:
                retjson['code'] = 400
                retjson['content'] = u'Arguments is empty'
            # elif re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", info_email) == None :
            #     retjson['code'] = 404
            #     retjson['content'] = u'Your email format is wrong'
            else:
                try:
                    # get the DBinfo of the person UID equals uid
                    t1 = self.db.query(UsersCache).filter(UsersCache.uid == uid)
                    # update the data of personal infomation 
                    t1.update({UsersCache.gender:gender,UsersCache.name:name,UsersCache.school:school,UsersCache.campus:campus,UsersCache.signature:signature,UsersCache.info_phone:info_phone})
                    self.db.query(User_tagCache).filter(User_tagCache.uid == uid).update({User_tagCache.user_enjoyment:tag})
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
            
        except Exception,e:
            print e
            retjson['code'] = 400
            retjson['content'] = u'Arguments is empty'
        ret = json.dumps(retjson,ensure_ascii=False, indent=2)
        print ret
        self.write(ret)


        
