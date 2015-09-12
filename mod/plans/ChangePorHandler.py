# -*- coding: utf-8 -*-
import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler

class ChangePorHandler(BaseHandler):
	def get(self):
		self.render('changePor.html',user=self.current_user)