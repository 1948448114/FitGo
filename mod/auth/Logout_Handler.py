# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache
#/auth/logout
class LogoutHandler(BaseHandler):
    def delete(self):#用户登出，删除cookie
        status = self.get_current_user()
        if status:
            # cookie = self.db.query(CookieCache).filter(CookieCache.cookie == status.cookie)
            self.db.remove(status)
            try:
                slef.db.commit()
            except:
                self.db.rollback()
        else:
            pass