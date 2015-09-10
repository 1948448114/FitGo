# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import TopicsCache

#/discover/discover_page
class DiscoverPageHandler(BaseHandler):
	def get(self):#发现主页面
		self.render('discoverpage.html',user=self.current_user)
	def post(self):
		try:
			topics = self.db.query(TopicsCache).order_by(TopicsCache.topic_time.desc())[0:12]
			if topics:
				retjson = {'code':200,'content':'success to query state'}
				content1 = []
				for n in topics:
					content = {}
					content['uid'] = n.uid
					content['topics_id'] = n.topics_id
					content['topic_time'] = n.topic_time
					content['topic_content'] = n.topic_content
					content['topic_pic '] = n.topic_pic
					content['topic_title '] = n.topic_title
					content['topic_starers'] = n.topic_starers 
					content1.append(content)
				retjson['content'] = content1
			else:
				retjson = {'code':400,'content':'have no state'}
		except Exception,e:
			print e
			retjson = {'code':400,'content':'failed to query state'}
		self.write(retjson)