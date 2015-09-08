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
		a = a_topic_title
		if a_topic_title:
			try:
				# print a_topic_title,type(a_topic_title),type(a)
				# print '0000000'
				# print "select * from Topics where topic_title like \'%%s\';" % a
				
				topics = self.db.execute("select * from Topics where topic_title like '%"+a_topic_title+"%';").fetchall()
				# topics = self.db.execute("select * from Topics where topic_title like '%';").all()
				# print '3333333',topics,type(topics)
				# top = self.db.execute("select * from Topics where topic_title like '%球.decode()%';")
				# print type(top),'eeeee',top
				#topics = self.db.execute("select * from Topics where topic_title like '%" + a_topic_title + "%';").all()
				# topics = self.db.execute("select * from Topics where topic_title like '%{$a_topic_title%';").all()
				# topics = self.db.query(TopicsCache).filter(TopicsCache.topic_title.like("%%s%")).all() % str(a_topic_title)
				# print '11111111'
				# print topics
				
				if topics:
					retjson = {'code':200,'content':'ok'}
					content1 = []
					for n in topics:
						content = {}
						content['uid'] = n.uid
						content['topic_id'] = n.topic_id
						content['topic_title'] = n.topic_title
						content['topic_content'] = n.topic_content
						content['topic_pic'] = n.topic_pic
						content['topic_starers'] = n.topic_starers
						content1.append(content)
					retjson['content'] = content1
					print retjson
					self.write(retjson)
				else:
					retjson = {'code':400,'content':'not match topics_title'}
					self.write(retjson)
			except Exception,e:
				print e
				retjson = {'code':400,'content':'failed to search state'}
				self.write(retjson)
		else:
			retjson = {'code':400,'content':'topic_title is null'}
			self.write(retjson)



