# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import TopicsCache,UsersCache

#/discover/discover_page
class DiscoverPageHandler(BaseHandler):
	def get(self):#发现主页面
		content=[
					{'square':'',
					'state_img':'1',
			       'id':'1',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'},
        			{'square':'',
					'state_img':'2',
			       'id':'2',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'},
        			{'square':'',
					'state_img':'3',
			       'id':'3',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'},
        			{'square':'',
					'state_img':'4',
			       'id':'4',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'},
        			{'square':'uc-container_square',
					'state_img':'5',
			       'id':'5',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'},
        			{'square':'uc-container_square',
					'state_img':'6',
			       'id':'6',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'},
        			{'square':'uc-container_square',
					'state_img':'7',
			       'id':'7',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'},
        			{'square':'uc-container_square',
					'state_img':'8',
			       'id':'8',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'},
        			{'square':'',
					'state_img':'9',
			       'id':'9',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'},
        			
        			{'square':'',
					'state_img':'10',
			       'id':'10',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'},
        			{'square':'',
					'state_img':'11',
			       'id':'11',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'},
        			{'square':'',
					'state_img':'12',
			       'id':'12',
                   'state_title':'lala',
        			'state_writer_link':'/plans',
        			'state_writer':'Andrew'}
        ]
		self.render('discoverpage.html',user=self.current_user,content=content)
	def post(self):
		times = self.get_argument("times")#刷新次数［0,1，2，。。。。］
		start = int(times)*11
		end = start + 11
		try:
			topics = self.db.query(TopicsCache).order_by((TopicsCache.topic_time+0).desc())[start:end]#topic_time参数格式未解决
			print type(TopicsCache.topic_time)
			if topics:
				retjson = {'code':200,'content':'success to query state'}
				content1 = []
				for n in topics:
					content = {}
					content['uid'] = n.uid
					user = self.db.query(UsersCache).filter(UsersCache.uid==n.uid).one()
					content['name'] = user.name
					content['topics_id'] = n.topic_id
					content['topic_time'] = n.topic_time
					content['topic_content'] = n.topic_content
					content['topic_pic'] = n.topic_pic
					content['pic_shape'] = n.pic_shape
					content['topic_title'] = n.topic_title
					content['topic_starers'] = n.topic_starers 
					content1.append(content)
				retjson['content'] = content1
			else:
				retjson = {'code':400,'content':'have no state'}
		except Exception,e:
			print e
			retjson = {'code':400,'content':'failed to query state'}
		self.write(retjson)