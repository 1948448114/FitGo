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
			# topics_count = self.db.query(func.count(topics))
			print topics_count,topics[0].uid,topics[1].uid
			print "======"
			# retjson = {'code':400,'content':topics[0].uid}
			retjson = {'code':400,'content':''}#{'uid':'','topic_id':''}
			# for n in topics:
			# 	print n
			retjson.content.push({'uid':topics[0].uid,"topic_id":topics[0].topic_id})

			self.write(retjson)

		except Exception,e:
			print e
			retjson = {'code':400,'content':'failed to search'}
			self.write(retjson)


