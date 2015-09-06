# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
import json
from ..databases.tables import TopicsCache
from mod.auth.Base_Handler import BaseHandler

#/discover/create
class CreateStateHandler(BaseHandler):
	def post(self):#发布动态
		user_id = self.get_argument('uid')
		a_topic_title = self.get_argument('topic_title')
		a_topic_content = self.get_argument('topic_content')
		a_topic_pic = self.get_argument('topic_pic')
		topics = TopicsCache(uid=user_id,topic_title=a_topic_title,topic_content=a_topic_content,topic_pic=a_topic_pic)
		self.db.add(topics)