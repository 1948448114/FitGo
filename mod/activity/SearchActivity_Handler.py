# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import ActCache
#/activity/search/
class SearchActivityHandler(BaseHandler):
	def post(self):#搜索活动
		user_id = self.get_argument("uid")
		a_act_title = self.get_argument("act_title")
		a_start_time = self.get_argument("start_time")
		a_end_time = self.get_argument("end_time")
		a_location = self.get_argument("location")

		try:
			activitys = self.db.query(ActCache).filter(ActCache.act_title==a_act_title).all()
			retjson = {'code':200,'content':'ok'}
			content1 = []
			for n in activitys:
				content = {}
				content['uid'] = n.uid
				content['act_id'] = n.act_id
				content['act_title'] = n.act_title
				content['start_time'] = n.start_time
				content['end_time'] = n.end_time
				content['act_location'] = n.location
				content['details'] = n.details
				content['join_people'] = n.join_people
				content1.append(content)
			retjson['content'] = content1
			print retjson
			self.write(retjson)
		except Exception,e:
			print e
			retjson = {'code':400,'content':'failed to search activity'}
			self.write(retjson)
