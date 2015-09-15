# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache,Invite_relation,UsersCache
import json,time
from time import mktime,strptime,strftime,time,localtime
from List import ListHandler
#/invite/unrespondlist
class UnResponseListHandler(BaseHandler):
	def get(self):#获得所有被拒绝的请求,state='2'
		arg_uid = self.current_user.uid
		ListHandler(self,arg_uid,'2')