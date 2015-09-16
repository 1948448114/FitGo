# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import InviteCache,UsersCache
import json,time,string

class HotHandler(BaseHandler):
	def get(self):
		retjson = {'code':200,'content':'Null'}
		contentall=[]
		time_now=time.time()
		sql_invite="select * from Invite where start_time >= %s order by start_time;" % str(time_now)
		sql_act = "select *from Act where start_time >= %s order by start_time;" % str(time_now)
		try:
			invitations=self.db.execute(sql_invite).fetchall()[0:2]
			for i in invitations:
				content={}
				content['start_time'] = time.strftime("%Y-%m-%d %H:%M",time.localtime(int(i.start_time)))
				content['fit_item'] = i.fit_item
				content['user_tag'] = i.user_tag
				content['remark'] = i.remark
				contentall.append(content)

			# activities=self.db.execute(sql_act).fetchall[0:1]
			# for n in activities:
			# 	content={}	
			# 	content['title'] = n.act_title
			# 	content['start'] = strftime("%Y-%m-%d",localtime(int(n.start_time)))
			# 	content['detail'] = n.act_detail
			# 	contentall.append(content)

			# state = self.Mongodb().Plan.find()
			
			# for i in state:
			# 	content={}
			# 	content['target']=i.target
			# 	content['signature']=i.signature
			# 	content['start_time']=i.start_time
			# 	content['end_time']=i.end_time
			# 	contentall.append(content)

			retjson['content'] = contentall
		except Exception, e:
			print e
			retjson['code'] = 401
			retjson['content'] = u'Nothing found!Please try other conditions'
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)