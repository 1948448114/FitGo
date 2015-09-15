# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache,Invite_relation,UsersCache
import json,time
#/invite/respondlist
class ResponseListHandler(BaseHandler):
	def get(self):#获得所有被同意的请求,state='1'
		arg_uid = self.current_user.uid
		retjson = {'code':200,'content':'ok'}
		try:
			content=[]
			response = self.db.query(Invite_relation).filter(Invite_relation.uid_respond==arg_uid,\
				Invite_relation.state == '1').order_by(Invite_relation.id.desc()).all()
			if response:
				for i in response:
					content1={}
					content1['uid_request'] = i.uid_request
					content1['uid_respond'] = i.uid_respond
					content1['state'] = i.state
					invitation = self.db.query(InviteCache).filter(InviteCache._id==i._id).one()
					request_user = self.db.query(UsersCache).filter(UsersCache.uid==i.uid_request).one()
					respond_user = self.db.query(UsersCache).filter(UsersCache.uid==i.uid_respond).one()
					content1['request_name'] = request_user.name
					content1['respond_name'] = respond_user.name
					if not request_user.info_phone:
						content1['request_phone'] = u'无'
					else:
						content1['request_phone'] = request_user.info_phone
					if not respond_user.info_phone:
						content1['respond_phone'] = u'无'
					else:
						content1['respond_phone'] = respond_user.info_phone
					# content1['start_time'] = invitation.start_time
					content1['start_time'] = time.strftime("%Y-%m-%d %H:%M",time.localtime(int(invitation.start_time)))
					content1['fit_location'] = invitation.fit_location
					content1['fit_item'] = invitation.fit_item
					content.append(content1)
			response = self.db.query(Invite_relation).filter(Invite_relation.uid_respond==arg_uid,\
				Invite_relation.state == '2').order_by(Invite_relation.id.desc()).all()
			
			for i in response:
				content1={}
				content1['state'] = i.state
				content1['_id'] = i._id
				invitation = self.db.query(InviteCache).filter(InviteCache._id==i._id).one()
				request_user = self.db.query(UsersCache).filter(UsersCache.uid==i.uid_request).one()
				respond_user = self.db.query(UsersCache).filter(UsersCache.uid==i.uid_respond).one()

				content1['request_name'] = request_user.name
				content1['respond_name'] = respond_user.name
				content1['request_phone'] = ''
				content1['respond_phone'] = ''
				# content1['start_time'] = invitation.start_time
				content1['start_time'] = time.strftime("%Y-%m-%d %H:%M",time.localtime(int(invitation.start_time)))
				content1['fit_location'] = invitation.fit_location
				content1['fit_item'] = invitation.fit_item
				content1['gender'] = invitation.gender
				content.append(content1)
			retjson['content'] = content
		except Exception, e:
			print str(e)
			retjson['code'] = 401
			retjson['content'] = u'No request!'
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		# self.write(ret)
		self.render('invite_request_all.html',content=retjson)