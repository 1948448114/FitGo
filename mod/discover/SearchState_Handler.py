# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import TopicsCache
# from sqlalchemy import func

#/discover/search/state
class SearchStateHandler(BaseHandler):
	def post(self):#搜索动态
		a_topic_title = self.get_argument('topic_title')

		try:
			topics = self.db.query(TopicsCache).filter(TopicsCache.topic_title==a_topic_title).all()
			retjson = {'code':400,'content':'ok'}
			content1 = []
			for n in topics:
				content = {}
				content['uid'] = n.uid
				content['topic_id'] = n.topic_id
				content1.append(content)
			retjson['content'] = content1
			print retjson
			self.write(retjson)

		except Exception,e:
			print e
			retjson = {'code':400,'content':'failed to search'}
			self.write(retjson)


