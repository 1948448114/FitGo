# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
#/activity/activity_page
class ActivityPageHandler(BaseHandler):
    def get(self):
        self.render('activity.html', user=self.current_user)
    def post(self):
    	pass
