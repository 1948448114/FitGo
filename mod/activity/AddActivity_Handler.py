# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import ActCache
#/activity/add
class AddActivityHandler(BaseHandler):
	def post(self):#参加活动
		pass