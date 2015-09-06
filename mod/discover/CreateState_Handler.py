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
		
		user_id = self.get_argument("uid")
		a_topic_title = self.get_argument('topic_title')
		a_topic_content = self.get_argument('topic_content')
		a_topic_pic = self.get_argument('topic_pic')
		
		try:
			topics = TopicsCache(uid=user_id,topic_title=a_topic_title,topic_content=a_topic_content,topic_pic=a_topic_pic)
			self.db.add(topics)
			retjson = {'code':400,'content':'ok'}
			try:
				self.db.commit()
			except:
				self.db.rollback()
				retjson['code'] = 401
				retjson['content'] = u'Database store is wrong!'
         
		except Exception,e:
			print e
			retjson = {'code':400,'content':'failed to create'}
		self.write(retjson)