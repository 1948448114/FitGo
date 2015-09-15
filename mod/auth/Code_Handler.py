# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache,PlansCache,ActCache
import json
from time import time
import uuid
import re
import math,uuid
import hashlib,random,string,os,Image,StringIO
from code import create_validate_code

class CodeHandler(BaseHandler):
	def get(self,code_time):
		code_time = hashlib.md5(str(code_time)).hexdigest()
		code_img = create_validate_code()
		con = {code_time:code_img[1]}
		try:
			self.Mongodb().Code.insert(con)
			s = StringIO.StringIO()
			code_img[0].save(s,"GIF")
			img_data = s.getvalue()
			s.close()
			self.set_header('Content-Type','image/gif')
			self.write(img_data)
		except Exception,e:
			retjson = {'code':200,'content':'ok'}
			retjson['code'] = 400
			retjson['content'] = 'Store code wrong!'
			ret = json.dumps(retjson,ensure_ascii=False, indent=2)
			self.write(ret)
		

	def identify_code(self,code_time,code) :
		try:
			code_time = hashlib.md5(str(code_time)).hexdigest()
			plan = self.Mongodb().Plan.find({code_time:code})
			if plan :
				return 0
			else :
				return 1
		except:
			return 1