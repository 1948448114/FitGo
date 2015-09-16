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
	def get(self):#获得用户所有历史请求，包括参与或者被参与的，同意的，不同意的
		arg_uid = self.current_user.uid
		# arg_uid = self.get_argument('uid')
		agree_list = ListHandler(self.db,arg_uid,'1') 
		disagree_list = ListHandler(self.db,arg_uid,'2')
		retjson = {'code':200,'content':'ok','agree_list':'','disagree_list':''}
		if agree_list['code'] == 200:
			retjson['agree_list'] = agree_list['content']
		else:
			retjson = agree_list
		if disagree_list['code'] == 200:
			retjson['disagree_list'] = disagree_list['content']
		else:
			retjson = disagree_list
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)

		# self.write(ret)
		self.render('invite_request_all.html',content=retjson)
