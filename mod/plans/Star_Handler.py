# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 
import tornado.web
import tornado.gen
import tornado.web
import tornado.gen
import json


from ..databases.tables import PlansCache
from ..databases.tables import UsersCache

from ..auth.Base_Handler import BaseHandler
#/plans/star/{plan_id}
class StarHandler(tornado.web.RequestHandler):
	@property
	def db(self):
		return self.application.db
	def on_finish(self):
		self.db.close()




	def post(self,plan_id):#计划点赞
		retjson = {'code':200,'content':'ok'}
		try:
			person = self.db.query(PlansCache).filter(PlansCache.plan_id == plan_id)

			person.update({PlansCache.grader:PlansCache.grader+1})
	
			try:
				self.db.commit()
				
			except Exception, e:
				self.db.rollback()
				retjson['code'] = 401
				retjson['content'] = u'Database store is wrong!'


		except Exception, e:
			print e
			retjson['code'] = 402
			retjson['content'] = "Sql store is wrong!Try again!"

		ret = json.dumps(retjson,ensure_ascii = False, indent = 2)
		self.write(ret)



		