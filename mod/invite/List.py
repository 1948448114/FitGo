# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache,Invite_relation,UsersCache
import json,time

def ListHandler(db,uid,state):
	arg_uid = uid
	retjson = {'code':200,'content':'ok'}
	try:
		response = db.query(Invite_relation).filter(Invite_relation.uid_respond==arg_uid,\
			Invite_relation.state == state).order_by(Invite_relation.id.desc()).all()
		content=[]
		if response:
			for i in response:
				content1={}
				content1['uid_request'] = i.uid_request
				content1['uid_respond'] = i.uid_respond
				content1['state'] = i.state
				invitation = db.query(InviteCache).filter(InviteCache._id==i._id).one()
				request_user = db.query(UsersCache).filter(UsersCache.uid==i.uid_request).one()
				respond_user = db.query(UsersCache).filter(UsersCache.uid==i.uid_respond).one()
				content1['request_name'] = request_user.name
				if not request_user.info_phone:
					content1['request_phone'] = u'无'
				else:
					content1['request_phone'] = request_user.info_phone
				content1['respond_name'] = respond_user.name
				if not respond_user.info_phone:
					content1['respond_phone'] = u'无'
				else:
					content1['respond_phone'] = respond_user.info_phone
				content1['start_time'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(invitation.start_time)))
				content1['fit_location'] = invitation.fit_location
				content1['fit_item'] = invitation.fit_item
				content.append(content1)
		request = db.query(Invite_relation).filter(Invite_relation.uid_request==arg_uid,\
			Invite_relation.state == state).order_by(Invite_relation.id.desc()).all() 
		if request:
			for i in request:
				content1={}
				content1['uid_request'] = i.uid_request
				content1['uid_respond'] = i.uid_respond
				content1['state'] = i.state
				invitation = db.query(InviteCache).filter(InviteCache._id==i._id).one()
				request_user = db.query(UsersCache).filter(UsersCache.uid==i.uid_request).one()
				respond_user = db.query(UsersCache).filter(UsersCache.uid==i.uid_respond).one()
				content1['request_name'] = request_user.name
				if not request_user.info_phone:
					content1['request_phone'] = u'无'
				else:
					content1['request_phone'] = request_user.info_phone
				content1['respond_name'] = respond_user.name
				if not respond_user.info_phone:
					content1['respond_phone'] = u'无'
				else:
					content1['respond_phone'] = respond_user.info_phone
				content1['start_time'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(invitation.start_time)))
				content1['fit_location'] = invitation.fit_location
				content1['fit_item'] = invitation.fit_item
				content.append(content1)
		retjson['content'] = content
	except Exception, e:
		print str(e)
		retjson['code'] = 401
		retjson['content'] = u'No request!'
	return retjson
	# ret = json.dumps(retjson,ensure_ascii=False, indent=2)
	# return ret
	# self.write(ret)
