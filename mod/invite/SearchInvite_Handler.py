# -*- coding: utf-8 -*-
#!/usr/bin/env python
# import tornado.web
# import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache
import json,time
#/invite/search/
class SearchInviteHandler(BaseHandler):
	def post(self):#搜索匹配者
		# t=time.time()
		retjson = {'code':200,'content':'ok'}

		sql = "select * from Invite where"
		string =""
		keys=('start_time','fit_location','fit_item','user_tag','gender')
		args=dict.fromkeys(keys)
		for key in args :
			args[key]=self.get_argument(key)
			if key == 'start_time' and key:
				string=string+' and start_time >= %s' % args['start_time']
			elif key == 'gender' and key:
				string=string+' and gender = \'%s\'' % args['gender']
			elif key:
				string=string+' and '+key+' like \'%'+args[key]+'%\''
		sql=sql+string[4:]+";"
		print sql
		try:
			invitations=self.db.execute(sql).fetchall()[0:40]
			content1 = []
			for i in invitations:
				content = {}
				content['uid'] = i.uid
				content['start_time'] = i.start_time
				content['duration'] = i.duration
				content['create_time'] = i.create_time
				content['fit_location'] = i.fit_location
				content['fit_item'] = i.fit_item
				content['user_tag'] = i.user_tag
				content['gender'] = i.gender
				content['remark'] = i.remark
				content['_id'] = i._id
				content1.append(content)
			retjson['content'] = content1
		except Exception, e:
			retjson['code'] = 401
			retjson['content'] = u'Nothing found!Please try other conditions'
		self.write(retjson)
