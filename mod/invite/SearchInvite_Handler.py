# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache
import json,time
#/invite/search/
class SearchInviteHandler(BaseHandler):
	def post(self):#搜索匹配者
		arg_start_time = self.get_argument("start_time")
		arg_fit_location = self.get_argument("fit_location")
		arg_fit_item = self.get_argument("fit_item")
		arg_user_tag = self.get_argument("user_tag")
		arg_gender = self.get_argument("gender")
		try:
			users=self.db.query(InviteCache).filter(InviteCache.start_time == arg_start_time).one()
			for u in users :
				print u
			print users
		except Exception, e:
			print e