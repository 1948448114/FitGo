# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache,Invite_relation,UsersCache
import json,time
import traceback
#/invite/respond
class RespondInviteHandler(BaseHandler):
	# @tornado.web.authenticated
	def put(self):
		retjson = {'code':200,'content':'ok'}
		try:
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
		except Exception,e:
			retjson = {'code':400,'content':'no parameters'}
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)
	# @tornado.web.authenticated
	def get(self):#get all 请求
		arg_uid = self.current_user.uid
		retjson = {'code':200,'content':'ok'}
		try:
			requests=self.db.query(Invite_relation).filter(Invite_relation.uid_respond==arg_uid,\
				Invite_relation.state == '0',Invite_relation.uid_request!=arg_uid).all()
			content=[]
			for i in requests:
				content1={}
				content1['uid_request'] = i.uid_request
				content1['uid_respond'] = i.uid_respond
				content1['state'] = i.state
				content1['_id'] = i._id
				try:
					invitation = self.db.query(InviteCache).filter(InviteCache._id==i._id).one()
					user = self.db.query(UsersCache).filter(UsersCache.uid==i.uid_request).one()
					content1['name'] = user.name
					content1['start_time'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(invitation.start_time)))
					content1['duration'] = invitation.duration
					content1['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(invitation.create_time)))
					content1['fit_location'] = invitation.fit_location
					content1['fit_item'] = invitation.fit_item
					content1['user_tag'] = invitation.user_tag

					content1['gender'] = user.gender
					content1['remark'] = invitation.gender
				except Exception,e:
					retjson['code'] = 402
					content1['name'] =  ''
					content1['start_time'] =  ''
					content1['duration'] =  ''
					content1['create_time'] =  ''
					content1['fit_location'] =  ''
					content1['fit_item'] = ''
					content1['user_tag'] = ''
					content1['gender'] = ''
					content1['remark'] = ''
				content.append(content1)
			retjson['content'] = content
		except Exception, e:
			retjson['code'] = 401
			retjson['content'] = u'No request!'
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.render('invite_request_item.html',content=retjson)
