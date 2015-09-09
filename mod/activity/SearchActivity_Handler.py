# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import ActCache
#/activity/search/
class SearchActivityHandler(BaseHandler):
	def post(self):#搜索活动
		a_act_title = self.get_argument("act_title")
		a_start_time = self.get_argument("start_time")
		a_location = self.get_argument("location")
		string = ''

		try:
			if a_act_title:
				string = string + 'act_title like \'%%%s%%\'' % a_act_title
			if a_start_time:
				string = string + 'start_time=\'%s\'' % a_start_time
			if a_location:
				string = string + 'user_name=\'%s\'' % a_username

			if string.strip()=='':
				retjson = {'code':400,'content':'all parameters are null'}
			else:
				activitys = self.db.execute("select * from Act where %s;" % string).fetchall()
				if activitys:
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
				else:
					retjson = {'code':400,'content':'not match activity'}
		except Exception, e:
			retjson = {'code':400,'content':'failed to search activity'}
		self.write(retjson)
