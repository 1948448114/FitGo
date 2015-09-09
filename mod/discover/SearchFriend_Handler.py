# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import UsersCache,User_tagCache

#/discover/search/friends
class SearchFriendHandler(BaseHandler):
	def post(self):#搜索好友
		a_username = self.get_argument('user_name')
		a_name = self.get_argument('name')
		a_campus = self.get_argument('campus')
		a_school = self.get_argument('school')
		#user_tag
		a_user_enjoyment = self.get_argument('user_enjoyment')
		a_user_join_times = self.get_argument('user_join_times')
		a_user_score = self.get_argument('user_score')
		a_user_join_event = self.get_argument('user_join_event')

		string = ''
		try:
			if a_username:
				string = string + 'user_name=\'%s\'' % a_username + ' and '
			if a_name:
				string = string + 'name=\'%s\'' % a_name + ' and '
			if a_campus:
				string = string + 'campus=\'%s\'' % a_campus + ' and '
			if a_school:
				string = string + 'school=\'%s\'' % a_school + ' and '
			if a_user_enjoyment:
				stirng = string + 'user_enjoyment like \'%%%s%%\'' % a_user_enjoyment + ' and '
			if a_user_join_times:
				string = string + 'user_join_times=\'%s\'' % a_user_join_times + ' and '
			if a_user_join_event:
				string = string + 'user_join_event=\'%s\'' % a_user_join_event  + ' and '
			if a_user_score:
				string = string + 'user_score=\'%s\'' % a_user_score
			print string
			print "select * from Users where %s;" % string
			if string.strip()=='':
				retjson = {'code':400,'content':'all parameters are null'}
			else:
				persons = self.db.execute("select * from Users where %s;" % string).fetchall()
				if persons:
					retjson = {'code':200,'content':'ok'}
					content1 = []
					for n in persons:
						content = {}
						content['uid'] = n.uid
						content1.append(content)
					retjson['content'] = content1
				else:
					retjson = {'code':400,'content':'not match friend'}	


		except Exception,e:
			print e
			retjson = {'code':400,'content':'failed to search friend'}
		self.write(retjson)


		