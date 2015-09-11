# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache,Invite_relation
import json,time
#/invite
class InviteHandler(BaseHandler):
	def post(self):#发布健身
		arg_uid = self.current_user.uid
		arg_start_time = self.get_argument("start_time")
		arg_duration = self.get_argument("duration")
		arg_create_time = int(time.time())
		# arg_create_time = self.get_argument("create_time")#arg_create_time = time.time()
		arg_fit_location = self.get_argument("fit_location")
		arg_fit_item = self.get_argument("fit_item")
		arg_user_tag = self.get_argument("user_tag")
		arg_gender = self.get_argument("gender")
		arg_remark = self.get_argument("remark")
		arg_id = time.time()
		retjson = {'code':200,'content':'ok'}
		if not arg_uid or not arg_user_tag or not arg_start_time :
			retjson['code'] = 400
			retjson['content'] = 'Some arguments are empty'
		else:
			try:
				arg_start_time = int(time.mktime(time.strptime(arg_start_time,"%Y-%m-%d %H:%M")))
				status = InviteCache(uid=arg_uid,start_time=arg_start_time,duration=arg_duration,\
					create_time=arg_create_time,fit_location=arg_fit_location,fit_item=arg_fit_item,\
					user_tag=arg_user_tag,gender=arg_gender,remark=arg_remark)
				self.db.add(status)
				try:
					self.db.commit()
				except Exception,e:
					self.db.rollback()
					retjson['code'] = 401
					retjson['content'] = u'Database store is wrong!'

			except Exception, e:
				self.db.rollback()
				retjson['code'] = 401
				retjson['content'] = u'Something bad in database!'
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)