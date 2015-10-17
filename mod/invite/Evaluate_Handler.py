# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import Invite_relation,InviteCache

class EvaluateHandler(BaseHandler):
	def get(self):#获取未评价的活动
		retjson = {'code':200,'content':'ok'}
		arg_uid = self.current_user.uid
		try:
			#获得所有作为参与者未评价的项目
			invitation_1 = self.db.execute("select * from Invite_relation where uid_request = %s and comment_state=1 and comment is null and score is null;" % arg_uid).fetchall()
			#获得所有作为发起者未评价的项目
			invitation_2 = self.db.execute("select * from Invite where uid = %s and comment_state=1 and comment is null and score is null;" % arg_uid).fetchall()
			content1 = []
			if invitation_1:
				for i in invitation_1:
					content = {}
					content['_id'] = n._id
					content['fit_item'] = n.fit_item
					content1.append(content)
			else:
				if invitation_2:
					for i in invitation_2:
						content = {}
						content['uid'] = i.uid
						content['name'] = i.name
						content['start_time'] = time.strftime("%Y-%m-%d %H:%M",time.localtime(int(i.start_time)))
						content['end_time'] = time.strftime("%Y-%m-%d %H:%M",time.localtime(int(i.end_time)))
						content['create_time'] = time.strftime("%Y-%m-%d %H:%M",time.localtime(int(i.create_time)))
						content['fit_location'] = i.fit_location
						content['fit_item'] = i.fit_item
						content['gender'] = i.gender
						content['remark'] = i.remark
						content['_id'] = i._id
						content1.append(content)
				else:
					retjson = {'code':400,'content':'no comment'}
				retjson['content'] = content1
		except Exception, e:
			retjson = {'code':400,'content':'failed to search comment'}
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)
	def post(self):#评论评分
		retjson = {'code':200,'content':'ok'}
		arg_uid = self.current_user.uid
		arg_id = self.get_argument('_id')
