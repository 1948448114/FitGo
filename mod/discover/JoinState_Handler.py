# -*- coding: utf-8 -*-

import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import TopicsCache,UsersCache
import json
import traceback

class JoinStateHandler(BaseHandler):
    def get(self):
        retjson = {'code':200,'content':'ok'}
        try:
            topic_id = self.get_argument('topic_id')
            if not topic_id:
                retjson['code'] = 400
                retjson['content'] = 'Parameter Lack'
            else:
                try:
                    # print act_id
                    topic = self.Mongodb().Topic.find_one({"_id":str(topic_id)}) 
                    if topic:
                        keys = act.keys()
                        content = []
                        for key in keys:
                            if key != '_id':
                                content.append({'uid':key,'name':topic[key]})
                        retjson['content'] = content
                    else:
                        Mongodb.Topic.insert({"_id":act_id})
                        retjson['content'] = []
                except:
                    print traceback.print_exc()
                    retjson['code'] = 500
                    retjson['content'] = 'SQL Error!'
        except:
            retjson['code'] = 400
            retjson['content'] = 'Parameter Lack'
        self.write(json.dumps(retjson,ensure_ascii=False,indent=2))
        # self.render('',content=retjson)


    def post(self):
        retjson = {'code':200,'content':'ok'}
        uid = self.get_argument("uid")
        topic_id = self.get_argument('topic_id')
        if not uid or not topic_id:
            retjson['code'] = 400
            retjson['content'] = 'Parameter Lack'
        else:
            try:
                user = self.db.query(UsersCache).filter(UsersCache.uid == uid).one()
                try:
                    topic = self.Mongodb().Topic
                    act.update({"_id":topic_id},{"$set":{uid:user.name}},True)
                except Exception,e:
                    print traceback.print_exc()
                    retjson['code'] = 500
                    retjson['content'] = 'SQL Error!'
            except Exception,e:
                print traceback.print_exc()
                retjson['code'] = 500
                retjson['content'] = 'SQL Error!'
        self.write(json.dumps(retjson,ensure_ascii=False,indent=2))