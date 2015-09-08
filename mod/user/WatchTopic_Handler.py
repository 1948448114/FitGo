# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
import tornado.web
import tornado.gen

from ..databases.tables import UsersCache 
from ..databases.tables import User_tagCache


from Base_Handler import BaseHandler


class UsertopicHandler(BaseHandler):
    """docstring for WatchUser_handler"""

    @property
    def db(self):
        return self.application.db


    def on_finish(self):
        self.db.close()


    def get(self):
        # 获取id
        # uid = self.get_argument('id')
        uid = 1

        person = self.db.query(UsersCache).filter(UsersCache.uid == uid).one()

        
        
        uid = person.uid
        name = person.name
        student_card = person.student_card
        student_id = person.student_id
        gender = person.gender
        user_name = person.user_name
        school = person.school
        campus = person.campus
        password = person.password
        info_email = person.info_email
        info_phone = person.info_phone
        portrait = person.portrait


        tags = self.db.query(User_tagCache).filter(User_tagCache.uid == uid).one()

        user_enjoyment = tags.user_enjoyment
        user_join_times = tags.user_join_times
        user_score = tags.user_score
        user_join_event = tags.user_join_event

        json = "{uid:"+str(uid)+",name:"+str(name)+",student_card:"+str(student_card)+",student_id:"+str(student_id)+",gender:"+str(gender)+",user_name:"+str(user_name)+",school:"+str(school)+",campus:"+str(campus)+",info_email:"+str(info_email)+",info_phone:"+str(info_phone)+",portrait:"+str(portrait)+",user_enjoyment:"+str(user_enjoyment)+",user_join_times:"+str(user_join_times)+",user_score:"+str(user_score)+",user_join_event:"+str(user_join_event)+"}"

        # json = "{totalPorperty:" + dt1.Rows[0]["totalPorperty"].ToString() + ",root:" + json + "}"

        self.render("userinfo.html",json=json,user = self.current_user)
        # self.write(json) 
