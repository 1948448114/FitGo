# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache
import json
#/invite
class InviteHandler(BaseHandler):
	def post(self):#发布邀请

		arg_uid = self.get_argument("uid")
		arg_start_time = self.get_argument("start_time")
		arg_duration = self.get_argument("duration")
		arg_create_time = self.get_argument("create_time")
		arg_fit_location = self.get_argument("fit_location")
		arg_fit_item = self.get_argument("fit_item")
		arg_user_tag = self.get_argument("user_tag")
		arg_gender = self.get_argument("gender")
		arg_remark = self.get_argument("remark")
		retjson = {'code':200,'content':'ok'}
		try:
			status = InviteCache(uid=arg_uid,start_time=arg_start_time,duration=arg_duration,\
				create_time=arg_create_time,fit_location=arg_fit_location,fit_item=arg_fit_item,\
				user_tag=arg_user_tag,gender=arg_gender,remark=arg_remark)
			self.db.add(status)
			try:
				self.db.commit()
			except:
				self.db.rollback()
				retjson['code'] = 401
				retjson['content'] = u'Database store is wrong!'
		except Exception, e:
			self.db.rollback()
			retjson['code'] = 401
			retjson['content'] = u'Something bad in database!'
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)