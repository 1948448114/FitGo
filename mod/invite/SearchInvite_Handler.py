# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache,UsersCache
import json,time,string
#/invite/search/
class SearchInviteHandler(BaseHandler):
	# @tornado.web.authenticated
	def post(self):#搜索匹配者
		# t=time.time()
		retjson = {'code':200,'content':'ok'}

		sql = "select * from Invite where uid!=\'%s\' and " % self.current_user.uid
		string =""
		keys=('start_time','fit_location','fit_item','user_tag','gender')
		args=dict.fromkeys(keys)
		state = 1
		for key in args :
			args[key]=self.get_argument(key)
			if key == 'start_time' and args[key]:
				state =0
				string=string+' and start_time >= %s' % args['start_time']
			elif key == 'gender' and args[key]:
				state =0
				string=string+' and gender = \'%s\'' % args['gender']
			elif args[key]:
				state =0
				string=string+' and '+key+' like \'%'+args[key]+'%\''
		if state:
			time_now=time.time()
			sql="select * from Invite where start_time >= %s order by start_time;" % str(time_now)
		else:
			sql=sql+string[4:]+" order by start_time;"
		print sql
		try:
			invitations=self.db.execute(sql).fetchall()[0:40]
			content1 = []
			for i in invitations:
				content = {}
				content['uid'] = i.uid
				user = self.db.query(UsersCache).filter(UsersCache.uid==i.uid).one()
				content['name'] = user.name
				content['portrait'] = user.portrait
				content['start_time'] = time.strftime("%Y-%m-%d %H:%M",time.localtime(int(i.start_time)))
				content['duration'] = i.duration
				content['create_time'] = time.strftime("%Y-%m-%d %H:%M",time.localtime(int(i.create_time)))
				content['fit_location'] = i.fit_location
				content['fit_item'] = i.fit_item
				content['user_tag'] = i.user_tag
				content['gender'] = i.gender
				content['remark'] = i.remark
				content['_id'] = i._id
				content1.append(content)
			retjson['content'] = content1
		except Exception, e:
			print e
			retjson['code'] = 401
			retjson['content'] = u'Nothing found!Please try other conditions'
		# self.write(retjson)
		self.render("invite_item.html",ret=retjson)