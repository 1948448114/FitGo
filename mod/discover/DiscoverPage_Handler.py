# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler,UsersCache
from ..databases.tables import TopicsCache
import traceback

#/discover/discover_page
class DiscoverPageHandler(BaseHandler):
    def get(self):#发现主页面
        self.render('discoverpage.html',user=self.current_user)
    def post(self):
        try:
            times = self.get_argument("times")#刷新次数［0,1，2，。。。。］
            start = int(times)*12
            end = start + 12
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
            self.render('discover_state.html',content=retjson)
        except Exception,e:
            print traceback.print_exc()
            print str(e)