# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen

#/discover/discover_page
class DiscoverPageHandler(tornado.web.RequestHandler):
	def get(self):#发现主页面
		self.render('discoverpage.html')