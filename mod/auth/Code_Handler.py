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
import hashlib,random,string,os,Image
from code import create_validate_code

class CodeHandler(BaseHandler):
	def get(self,codes):
		retjson = {'code':200,'content':'ok'}
		code_name = hashlib.md5(codes.join(str(uuid.uuid1()))).hexdigest()+'.gif'
		try:
			code_img = create_validate_code()
			outfile = os.path.join(os.path.dirname('static')+'static/idcode',code_name)
			code_img[0].save(outfile,"GIF")
			retjson['content'] = '/'+outfile
			con = {outfile[:-4]:code_img[1]}
			try:
				self.Mongodb().Code.insert(con)# % code_name
			except Exception,e:
				retjson['code'] = 400
				retjson['content'] = 'Store code wrong!'
		except Exception,e:
			self.db.rollback()
			retjson['code'] = 401
			retjson['content'] = u'Get code wrong!'
		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
		self.write(ret)
	def identify_code(self,outfile,code) :
		try:
			plan = self.Mongodb().Plan.find({outfile[:-4]:code})
			if plan :
				return 0
			else :
				return 1
		except:
			return 1