# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import TopicsCache
from time import mktime,strptime,strftime,time,localtime
import json,string
# from sqlalchemy import func

#/discover/search/state
class SearchStateHandler(BaseHandler):
	def post(self):#搜索动态
		a_topic_title = self.get_argument('topic_title')
		a = a_topic_title
		if a_topic_title:
			try:

				print "select * from Topics where topic_title like \'%%%s%%\';" % a
				
				topics = self.db.execute("select * from Topics where topic_title like \'%%%s%%\';" % a_topic_title).fetchall()

				
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
						content['pic_shape'] = n.pic_shape
						content['topic_time'] = strftime("%Y-%m-%d",localtime(string.atoi(n.topic_time)))
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
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)