# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache,Invite_relation,UsersCache
import json,time
from List import ListHandler
#/invite/respondlist
class ResponseListHandler(BaseHandler):
	def get(self):#获得所有被同意的请求,state='1'
		arg_uid = self.current_user.uid
		ListHandler(self,arg_uid,'1')