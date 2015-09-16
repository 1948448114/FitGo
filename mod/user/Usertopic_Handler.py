# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
import json
from ..databases.tables import TopicsCache
from ..auth.Base_Handler import BaseHandler



class UsertopicHandler(BaseHandler):
    """docstring for WatchUser_handler"""
    def get(self):
        self.render("userinfo.html",user = self.current_user)

    def post(self):
        # 获取id
        uid = self.get_argument('id')
        # person = self.db.query(UsersCache).filter(UsersCache.uid == uid).one()
        topics = self.db.query(TopicsCache).filter(TopicsCache.uid == uid).all()
        rejson = {'code':200,'content':'ok'}
        content1 = []
        for row in topics:
            content={}
            topic_content = row.topic_content
            topic_title = row.topic_title
            topic_starers = row.topic_starers

            content['topic_content'] = str(topic_content)
            content['topic_title'] = str(topic_title)
            content['topic_starers'] = str(topic_starers)
            content1.append(content)
        rejson['content'] = content1
            # json = json + "{uid:"+str(uid)+",topic_id:"+str(topic_id)+",topic_content:"+str(topic_content)+",topic_pic:"+str(topic_pic)+",topic_title:"+str(topic_title)+",topic_starers:"+str(topic_starers)+"}"
        ret = json.dumps(rejson,ensure_ascii = False, indent = 2)
        # json = "{"+json+"}"
        self.write(ret)

       
      
