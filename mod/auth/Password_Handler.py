# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache
from sqlalchemy.orm.exc import NoResultFound
import json
from time import time
import uuid
import re

class PasswordHandler(BaseHandler):
	# @tornado.web.authenticated
	def put(self):
		old_passwd = self.get_argument('old_password')
		new_passwd = self.get_argument('new_password')
		user_cookie = self.current_user
		retjson = {"code":200,"content":""}
		try:
			usr1=self.db.query(UsersCache).filter(UsersCache.uid==user_cookie.uid,UsersCache.password==old_passwd).one()
			usr1.password = new_passwd
			self.db.add(usr1)
			retjson['content'] = "passwd update ok!"
			try:
				self.db.commit()
			except Exception,e:
				self.db.rollback()
				retjson['code'] = 400
				retjson['content'] = 'store data wrong!Try again'
		except NoResultFound:
			retjson['code'] = 400
			retjson['content'] = 'Please check your old password'
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)
	def post(self):
		try:
			arg_info_email = self.get_argument('info_email')
			arg_student_card = self.get_argument('student_card')
			arg_student_id = self.get_argument('student_id')
			arg_new_password = self.get_argument('new_password')
			retjson = {"code":200,"content":""}
			try:
				user = self.db.query(UsersCache).filter(UsersCache.info_email==arg_info_email,\
					UsersCache.student_id==arg_student_id,UsersCache.student_card==arg_student_card).one()
				if user:
					user.password = arg_new_password
					self.db.add(user)
					retjson['content'] = "passwd update ok!"
				else:
					retjson = {'code':400,'content':'no user'}
				try:
					self.db.commit()
				except Exception,e:
					self.db.rollback()
					retjson['code'] = 400
					retjson['content'] = 'store data wrong!Try again'
			except Exception,e:
				retjson = {'code':400,'content':'failed to query database'}
		except Exception,e:
			retjson = {'code':400,'content':'no parameters'}
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)
		
