# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
#/discover/add
class AddFriendHandler(BaseHandler):
	def post(self):#添加好友
		pass