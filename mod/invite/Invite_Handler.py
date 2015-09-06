# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
#/invite/{uid}
class InviteHandler(BaseHandler):
	def post(self):#发布邀请
		pass