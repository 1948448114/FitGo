# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 
import tornado.web
import tornado.gen
import tornado.web
import tornado.gen
import json


from ..databases.tables import PlansCache
from ..databases.tables import UsersCache

from ..auth.Base_Handler import BaseHandler


class PlansHandler(BaseHandler):
    """docstring for WatchUser_handler"""

    @property
    def db(self):
        return self.application.db


    def on_finish(self):
        self.db.close()

    def get(self,user_id):
        self.render("plans.html",user = self.current_user)



    def post(self,user_id):
        # 获取id
        # uid = self.get_argument('id')

        retjson = {'code':200,'content':'ok'}

        uid = user_id
        plan_id = self.get_argument('plan_id')
        create_time = self.get_argument('create_time') 
        start_time = self.get_argument('start_time') 
        end_time = self.get_argument('end_time') 
        fit_location = self.get_argument('fit_location') 

        fit_item = self.get_argument('fit_item') 
        remark = self.get_argument('remark') 
        grader = self.get_argument('grader') 

      
        # self.write(uid+plan_id+create_time+fit_item+grader)

        if not uid or not create_time or not start_time or not end_time or not fit_location or not fit_item or not remark or not grader:
            retjson['code'] = 400
            retjson['content'] = u'Arguments is empty'

        else:
            try:
            	status_plans = PlansCache(uid = uid,plan_id = plan_id,create_time = create_time,start_time = start_time,end_time = end_time,fit_location = fit_location,fit_item = fit_item,remark = remark,grader = grader)
            	self.db.add(status_plans)
            	   #              status_users = UsersCache(student_card = arg_student_card,student_id = arg_student_id,uid = uid_uuid,info_email = arg_info_email)
                # self.db.add(status_users)

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



        
