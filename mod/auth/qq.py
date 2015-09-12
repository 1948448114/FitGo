# -*- coding: utf-8 -*-
#!/usr/bin/env python
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache
import json

class qqHandler(BaseHandler):
	def post(self):
		arg_openid = self.get_argument('openid')
		arg_name = self.get_argument('name')
		arg_gender = self.get_argument('gender')
		arg_portrait = self.get_argument('portrait')
		print arg_openid,arg_name
		# cookie_uuid=uuid.uuid1()
  #       self.set_secure_cookie("username",str(cookie_uuid),expires_days=30,expires=int(time())+2592000)
		# status_cookie = CookieCache(cookie=cookie_uuid,uid=arg_uid)
		# self.db.add(status_cookie)
		# #commit to sql
		# try:
  #                 self.db.commit()
  #               except Exception, e:
  #                   self.db.rollback()
  #                   retjson['code'] = 401
  #                   retjson['content'] = u'Database store is wrong!'