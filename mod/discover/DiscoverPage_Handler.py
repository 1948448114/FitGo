# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler

#/discover/discover_page
class DiscoverPageHandler(BaseHandler):
	def get(self):#发现主页面
		self.render('discoverpage.html',user=self.current_user)