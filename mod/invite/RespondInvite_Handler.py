# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache,Invite_relation
import json,time
import traceback
#/invite/respond
class RespondInviteHandler(BaseHandler):
	# @tornado.web.authenticated
	def put(self):
		retjson = {'code':200,'content':'ok'}
		arg_uid_respond = self.current_user.uid
		arg_id = self.get_argument('_id')
		arg_uid_request = self.get_argument('uid_request')
		arg_code = self.get_argument('code')
		try:
			requests=self.db.query(Invite_relation).filter(\
				Invite_relation.uid_respond==arg_uid_respond,\
				Invite_relation.uid_request == arg_uid_request,\
				Invite_relation._id ==arg_id)
			requests.update({Invite_relation.state : arg_code})
			self.db.commit()
		except Exception, e:
			self.db.rollback()
			retjson['code'] = 401
			retjson['content'] = u'Database store _id is wrong!'
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)
	# @tornado.web.authenticated
	def get(self):#get all 请求
		arg_uid = self.current_user.uid
		retjson = {'code':200,'content':'ok'}
		try:
			requests=self.db.query(Invite_relation).filter(Invite_relation.uid_respond==arg_uid,\
				Invite_relation.state == '0').all()
			# print requests
			content=[]
			for i in requests:
				print i.uid_respond
				content1={}
				content1['uid_request'] = i.uid_request
				content1['uid_respond'] = i.uid_respond
				content1['state'] = i.state
				content1['_id'] = i._id
				content.append(content1)
			retjson['content'] = content
		except Exception, e:
			print e
			print traceback.print_exc()
			retjson['code'] = 401
			retjson['content'] = u'No request!'
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)