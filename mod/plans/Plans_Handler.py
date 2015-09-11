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
import json


class PlansHandler(BaseHandler):
     """
     get函数：
        展示plan主页面
     post函数:
        发表plan

    plan的json格式:
        {
            '_id':'',
            'content':{
                'target':'',
                'signature':'',
                'start_time':'',
                'end_time':'',
                'Mon':{
                    'oxygen':'',
                    'noxygen':'',
                    'lashen':''
                },
                'Tue':{
                    'oxygen':'',
                    'noxygen':'',
                    'lashen':''
                },
                'Wed':{
                    'oxygen':'',
                    'noxygen':'',
                    'lashen':''
                },
                'Thu':{
                    'oxygen':'',
                    'noxygen':'',
                    'lashen':''
                },
                'Fri':{
                    'oxygen':'',
                    'noxygen':'',
                    'lashen':''
                },
                'Sat':{
                    'oxygen':'',
                    'noxygen':'',
                    'lashen':''
                },
                'Sun':{
                    'oxygen':'',
                    'noxygen':'',
                    'lashen':''
                }
            },
            'star':{
                {uid}:{name}
                ...
            }
        }
     """

     def get(self):
        self.render("plans.html", user=self.current_user)

     def post(self):
        retjson = {'code':200,'content':'ok'}
        planJson = self.get_argument('plan')
        try:
            self.Mongodb().Plan.insert(json.loads(planJson))
        except Exception,e:
            print e
            retjson['code'] = 400
            retjson['content'] = 'New Plan Error!'
        ret = json.dumps(retjson,ensure_ascii=False, indent=2)
        self.write(ret)


