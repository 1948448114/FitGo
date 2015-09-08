# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache,InviteCache
#/invite/search/
class SearchInviteHandler(BaseHandler):
	def post(self):#搜索匹配者
		pass