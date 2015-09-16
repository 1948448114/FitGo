# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache

class FindPasswordHandler(BaseHandler):
	def post(self):
		try:
			arg_info_email = self.get_argument('info_email')
			arg_student_card = self.get_argument('student_card')
			arg_student_id = self.get_argument('student_id')
			try:
				self.db.query(UsersCache).filter(UsersCache.info_email==arg_info_email,\
					UsersCache.student_id==student_id,UsersCache.student_card==student_card).one()
			except Exception,e:
				retjson = {'code':400,'content':'failed to query '}
		except Exception,e:
			retjson = {'code':400,'content':'no parameters'}