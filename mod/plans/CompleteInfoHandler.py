# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler

class CompleteInfoHandler(BaseHandler):
	def get(self):
		self.render('completeInfo.html',user=self.current_user)