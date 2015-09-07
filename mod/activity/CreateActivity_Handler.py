# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import ActCache
#/activity/create
class CreateActivityHandler(BaseHandler):
	def post(self):#发起活动
		user_id = self.get_argument("uid")
		a_activity_title = self.get_argument("activity_title")
		a_start_time = self.get_argument("start_time")
		a_end_time = self.get_argument("end_time")
		a_location = self.get_argument("location")
		a_details = self.get_argument("details")

		try:
			activity = ActCache(uid=user_id,activity_title=a_activity_title,\
				start_time=a_start_time,end_time=a_end_time,location=a_location,details=a_details)
			self.db.add(activity)
			retjson = {'code':200,'content':'ok'}
			try:
				self.db.commit()
			except:
				self.db.rollback()
				retjson['code'] = 401
				retjson['content'] = u'Database store is wrong!'
         
		except Exception,e:
			print e
			retjson = {'code':400,'content':'failed to create activity'}
		self.write(retjson)
