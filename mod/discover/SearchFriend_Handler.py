# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import UsersCache,User_tagCache

#/discover/search/friends
class SearchFriendHandler(BaseHandler):
	def post(self):#搜索好友
		a_username = self.get_argument('username')
		a_name = self.get_argument('name')
		a_campus = self.get_argument('campus')
		a_school = self.get_argument('school')
		#user_tag
		a_user_enjoyment = self.get_argument('user_enjoyment')
		a_user_join_times = self.get_argument('user_join_times')
		a_user_score = self.get_argument('user_score')
		a_user_join_event = self.get_argument('user_join_event')

		try:
			person = self.db.query(UsersCache).filter(UsersCache.user_name==a_username)
		except Exception,e:
			print e



		