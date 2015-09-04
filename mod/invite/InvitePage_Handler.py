# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
#/invite/user_page
class InvitePageHandler(BaseHandler):
	def get(self):#约健身主页
		self.render('invite.html', user=self.current_user)