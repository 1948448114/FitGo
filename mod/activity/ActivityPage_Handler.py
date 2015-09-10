# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from ..auth.Base_Handler import BaseHandler
from ..databases.tables import ActCache
from time import mktime,strptime,strftime,time,localtime
from sqlalchemy.orm.exc import NoResultFound
from ActivityController import getJoinUid
import json,string
#/activity/activity_page
class ActivityPageHandler(BaseHandler):
    def get(self):
        self.render('activity.html', user=self.current_user)
    def post(self):
        nowtime = int(time())
        retjson = {'code':200,'content':''}
        try:
            act = self.db.query(ActCache).filter(ActCache.create_time>nowtime-86400).order_by(ActCache.act_id.desc())
            all_content = []
            for i in act:
                contentTemp = {
                    'id':i.act_id,
                    'uid':i.uid,
                    'create_time':strftime("%Y-%m-%d",localtime(string.atoi(i.create_time))),
                    'title':i.act_title,
                    'start':i.start_time,
                    'end':i.end_time,
                    'location':i.act_location,
                    'detail':i.act_detail,
                    'join_uid':getJoinUid(i.act_id,self.Mongodb())
                }
                all_content.append(contentTemp)
            retjson['content'] = all_content
        except NoResultFound:
            retjson['code'] = 402
            retjson['content'] = 'No fresh content'
        self.render('activity_item.html',ret=retjson)
        # self.write(json.dumps(retjson,ensure_ascii=False, indent=2))
