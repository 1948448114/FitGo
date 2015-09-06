# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
import tornado.web
import tornado.gen
import json

from ..databases.tables import UsersCache 
from ..databases.tables import User_tagCache

from Base_Handler import BaseHandler


class UserinfoHandler(BaseHandler):
    """docstring for WatchUser_handler"""

    @property
    def db(self):
        return self.application.db


    def on_finish(self):
        self.db.close()


    def get(self):
        
        self.render("userinfo.html",user = self.current_user)

    def post(self,user_id):
        # 获取id
        # uid = self.get_argument('id')
        uid = user_id

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

        rejson = {'code':200,'content':'ok'}

        content = {'uid':'100'}

        content['uid'] = str(uid)

        content['name'] = str(name)

        content['student_card'] = str(student_card)

        content['student_id'] = str(student_id)
        content['gender'] = str(gender)
        content['user_name'] = str(user_name)
        content['school'] = str(school)
        content['campus'] = str(campus)
        content['info_email'] = str(info_email)
        content['info_phone'] = str(info_phone)
        content['portrait'] = str(portrait)
        content['user_enjoyment'] = str(user_enjoyment)
        content['user_join_times'] = str(user_join_times)
        content['user_score'] = str(user_score)
        content['user_join_event'] = str(user_join_event)
      

        rejson['content'] = content

        ret = json.dumps(rejson,ensure_ascii = False, indent = 2)

        self.write(ret)
		


        # json = "{uid:"+str(uid)+",name:"+str(name)+",student_card:"+str(student_card)+",student_id:"+str(student_id)+",gender:"+str(gender)+",user_name:"+str(user_name)+",school:"+str(school)+",campus:"+str(campus)+",info_email:"+str(info_email)+",info_phone:"+str(info_phone)+",portrait:"+str(portrait)+",user_enjoyment:"+str(user_enjoyment)+",user_join_times:"+str(user_join_times)+",user_score:"+str(user_score)+",user_join_event:"+str(user_join_event)+"}"

        # json = "{totalPorperty:" + dt1.Rows[0]["totalPorperty"].ToString() + ",root:" + json + "}"

        
        # self.write(json) 


		 



	 	# self.render("index.html", json=person)







