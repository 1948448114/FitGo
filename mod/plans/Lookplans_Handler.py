# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 
import tornado.web
import tornado.gen
import tornado.web
import tornado.gen
import json


from ..databases.tables import PlansCache
from ..databases.tables import UsersCache

from ..auth.Base_Handler import BaseHandler

# 此类：得到用户计划列表
class LookplansHandler(BaseHandler):
    """
    get函数：
        根据用户id，返回该用户所有plan
    """
    def get():
        retjson = {'code':200,'content':'ok'}
        try:
            uid = self.get_argument('uid')
            if not uid:
                retjson['code'] = 400
                retjson['content'] = 'Parameter Lack'
            else:
                try:
                    plan = self.Mongodb().Plan.find({'uid':uid})
                    content = []
                    for i in plan:
                        content.append(i)
                    retjson['content'] = content
                except:
                    retjson['code'] = 500
                    retjson['code'] = 'SQL Error!'
        except:
            retjson['code'] = 400
            retjson['content'] = 'Parameter Lack'
        ret = json.dumps(retjson,ensure_ascii=False, indent=2)
        self.write(ret)



