# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import ActCache
#/activity/activity_page
class ActivityPageHandler(BaseHandler):
    def get(self):
        self.render('activity.html', user=self.current_user)
    def post(self):
        act = self.db.query(ActCache).order_by(ActCache.act_id)[0:9]
        for i in act:
            print i.act_id

