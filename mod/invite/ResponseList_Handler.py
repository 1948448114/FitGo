# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache,Invite_relation,UsersCache
import json,time
#/invite/respondlist
class ResponseListHandler(BaseHandler):
	def get():#获得所有被同意的请求,state='1'
		arg_uid = self.current_user.uid
		print arg_uid
		retjson = {'code':200,'content':'ok'}
		try:
			response = self.db.query(Invite_relation).filter(Invite_relation.uid_respond==arg_uid,\
				Invite_relation.state == '1').all()
			content=[]
			for i in response:
				content1={}
				content1['uid_request'] = i.uid_request
				content1['uid_respond'] = i.uid_respond
				content1['state'] = i.state
				content1['_id'] = i._id
				invitation = self.db.query(InviteCache).filter(InviteCache._id==i._id).one()
				print invitation._id
				user = self.db.query(UsersCache).filter(UsersCache.uid==i.uid_request).one()
				print user.name
				content1['name'] = user.name
				content1['start_time'] = invitation.start_time
				content1['duration'] = invitation.duration
				content1['create_time'] = invitation.create_time
				content1['fit_location'] = invitation.fit_location
				content1['fit_item'] = invitation.fit_item
				content1['user_tag'] = invitation.user_tag
				content1['gender'] = invitation.gender
				content1['remark'] = invitation.remark
				content.append(content1)
			retjson['content'] = content
		except Exception, e:
			retjson['code'] = 401
			retjson['content'] = u'No request!'
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)