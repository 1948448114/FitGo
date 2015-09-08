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

# 此类：得到用户计划列表
class LookplansHandler(BaseHandler):
    """docstring for WatchUser_handler"""

    @property
    def db(self):
        return self.application.db


    def on_finish(self):
        self.db.close()

    # render里面的值可以改成自己写的html文件
    def get(self):
        self.render("lookplans.html",user = self.current_user)


    #获取uid 得到计划 
    def post(self,user_id):
        # 获取id
        # uid = self.get_argument('id')
        uid = user_id

        

        # person = self.db.query(UsersCache).filter(UsersCache.uid == uid).one()
        # self.write(person.uid)
        plans = self.db.query(PlansCache).filter(PlansCache.uid == uid).all()


        rejson = {'code':200,'content':'ok'}

        content1 = []
        
        for row in plans:
            
            content={}

            plan_id = row.plan_id
            create_time = row.create_time
            start_time = row.start_time
            end_time = row.end_time
            fit_location = row.fit_location
            fit_item = row.fit_item
            remark = row.remark
            grader = row.grader


            content['uid'] = str(uid)
            content['create_time'] = str(create_time)
            content['plan_id'] = str(plan_id)
            content['start_time'] = str(start_time)
            content['end_time'] = str(end_time)
            content['fit_location'] = str(fit_location)
            content['fit_item'] = str(fit_item)
            content['remark'] = str(remark)
            content['grader'] = str(grader)




            content1.append(content)
        rejson['content'] = content1

            # json = json + "{uid:"+str(uid)+",topic_id:"+str(topic_id)+",topic_content:"+str(topic_content)+",topic_pic:"+str(topic_pic)+",topic_title:"+str(topic_title)+",topic_starers:"+str(topic_starers)+"}"

        ret = json.dumps(rejson,ensure_ascii = False, indent = 2)

        # json = "{"+json+"}"
        self.write(ret)