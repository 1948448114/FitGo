#-*- coding: UTF-8 -*-
from mod.auth.Base_Handler import BaseHandler
import pymongo
import tornado.web
import tornado.gen
import tornado.web
import tornado.gen
import json


from pymongo import MongoClient

from ..databases.tables import UsersCache,CookieCache
#/discover/add
class RecomUserHandler(BaseHandler):
    @property
    def db(self):
        return self.application.db


    @property
    def Mongodb(self):
      return self.application.Mongodb


    def on_finish(self):
        self.db.close()

    def post (self):

      rejson = {'code':200,'content':'ok'}
      # uid
      user_cookie = self.current_user
      uid = user_cookie.uid

      person = self.db.query(UsersCache).filter(UsersCache.uid == uid).one()
      # self.write(str(person.cos))
      cos = float(person.cos)
      users = self.db.query(UsersCache).filter((UsersCache.cos-cos)>-0.9, (UsersCache.cos-cos) < 0.9 ).all()
      users.sort(key = lambda obj:abs(obj.cos-cos),reverse=False)
      
      content1=[]
      n = 1
      for user in users:
        if n > 10:
          break
        n = n + 1
        content = {}
        if user.uid !=uid :
          content['uid'] = str(user.uid)
          content['xiangsidu'] = str(100*(1-abs(user.cos-cos)))+"%"
          
          content['name'] = str((user.name).encode('utf-8'))
          content['signature'] = str((user.signature).encode('utf-8'))
          content['portrait'] = str(user.portrait)
          content1.append(content)


      rejson['content'] = content1

            
      ret = json.dumps(rejson,ensure_ascii = False, indent = 2)

       
      self.write(ret)

        
