# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
import tornado.web
import tornado.gen
import json


from ..databases.tables import TopicsCache

from Base_Handler import BaseHandler


class UsertopicHandler(BaseHandler):
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

        

        # person = self.db.query(UsersCache).filter(UsersCache.uid == uid).one()
        topics = self.db.query(TopicsCache).filter(TopicsCache.uid == uid).all()


        rejson = {'code':200,'content':'ok'}

        content1 = []
        
        for row in topics:
          
            content={}
            topic_id = row.topic_id
            uid = row.uid
            topic_content = row.topic_content
            topic_pic = row.topic_pic
            topic_title = row.topic_title
            topic_starers = row.topic_starers

            content['uid'] = str(uid)
            content['topic_id'] = str(topic_id)
            content['topic_content'] = str(topic_content)
            content['topic_pic'] = str(topic_pic)
            content['topic_title'] = str(topic_title)
            content['topic_starers'] = str(topic_starers)
            content1.append(content)
        rejson['content'] = content1

            # json = json + "{uid:"+str(uid)+",topic_id:"+str(topic_id)+",topic_content:"+str(topic_content)+",topic_pic:"+str(topic_pic)+",topic_title:"+str(topic_title)+",topic_starers:"+str(topic_starers)+"}"

        ret = json.dumps(rejson,ensure_ascii = False, indent = 2)

        # json = "{"+json+"}"
        self.write(ret)

       
      



        # uid = person.uid
        # name = person.name
        # student_card = person.student_card
        # student_id = person.student_id
        # gender = person.gender
        # user_name = person.user_name
        # school = person.school
        # campus = person.campus
        # password = person.password
        # info_email = person.info_email
        # info_phone = person.info_phone
        # portrait = person.portrait


        # tags = self.db.query(User_tagCache).filter(User_tagCache.uid == uid).one()

        # user_enjoyment = tags.user_enjoyment
        # user_join_times = tags.user_join_times
        # user_score = tags.user_score
        # user_join_event = tags.user_join_event

        # json = "{uid:"+str(uid)+",name:"+str(name)+",student_card:"+str(student_card)+",student_id:"+str(student_id)+",gender:"+str(gender)+",user_name:"+str(user_name)+",school:"+str(school)+",campus:"+str(campus)+",info_email:"+str(info_email)+",info_phone:"+str(info_phone)+",portrait:"+str(portrait)+",user_enjoyment:"+str(user_enjoyment)+",user_join_times:"+str(user_join_times)+",user_score:"+str(user_score)+",user_join_event:"+str(user_join_event)+"}"

        # # json = "{totalPorperty:" + dt1.Rows[0]["totalPorperty"].ToString() + ",root:" + json + "}"

        # self.render("userinfo.html",json=json,user = self.current_user)
        # # self.write(json) 


		 



	 	# self.render("index.html", json=person)



