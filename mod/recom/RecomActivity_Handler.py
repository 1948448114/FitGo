#-*- coding: UTF-8 -*-
from mod.auth.Base_Handler import BaseHandler
import pymongo
import tornado.web
import tornado.gen
import tornado.web
import tornado.gen
import json


from pymongo import MongoClient

from ..databases.tables import UsersCache,CookieCache,ActCache
#/discover/add
class RecomActivityHandler(BaseHandler):
    @property
    def db(self):
        return self.application.db


    @property
    def Mongodb(self):
      return self.application.Mongodb


    def on_finish(self):
        self.db.close()

    def post (self):
      """
        推荐活动，不需要参数，post方法。返回json值。json值是推荐的活动集合
      """

      rejson = {'code':200,'content':'ok'}
      # uid
      user_cookie = self.current_user
      uid = user_cookie.uid

      person = self.db.query(ActCache).filter(ActCache.uid == uid).first()

      # cos = float(person.cos)
      if person is None:
        print 'person is none '
        cos = 0.0
        acts = self.db.query(ActCache).filter().all() 

      else:
        # cos = float(person.cos)
        cos = person.cos
        act_title = person.act_title
        acts = self.db.query(ActCache).filter(ActCache.act_title == act_title,ActCache.uid != uid).all()

      acts.sort(key = lambda obj:abs(obj.cos-cos),reverse=False)
      content1=[]
      n = 1
      for act in acts:
        # print act.uid
        if n >20:
          break
        n = n + 1
        content = {}
        content['uid'] = str(act.uid)
        content['act_id'] = str(act.act_id)
        content['create_time'] = str(act.create_time)
        content['end_time'] = str(act.end_time)
        content['start_time'] = str(act.start_time)
        if act.act_location is None:
          content['act_location'] = str((act.act_location))
        else:
        # else:  
          content['act_location'] = str((act.act_location).encode('UTF-8'))
        if act.act_title is None:
          content['act_title'] = str((act.act_title))
        else:
          content['act_title'] = str((act.act_title).encode('UTF-8'))
        if act.act_detail is None:
          content['act_detail'] = str((act.act_detail))
        else:
          content['act_detail'] = str((act.act_detail).encode('UTF-8'))
          

        content1.append(content)
     

      rejson['content'] = content1

            
      ret = json.dumps(rejson,ensure_ascii = False, indent = 2)

       
      self.write(ret)

        
