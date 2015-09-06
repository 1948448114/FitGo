# -*- coding: utf-8 -*-
#!/usr/bin/env python
import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache,CookieCache
#/auth/logout
class LogoutHandler(BaseHandler):
    def delete(self):#用户登出，删除cookie
        status = self.current_user
        print status.cookie
        if status:
            # cookie = self.db.query(CookieCache).filter(CookieCache.uid == status.uid).all()
            self.db.delete(status)
            try:
                self.db.commit()
            except Exception,e:
                print e
                self.db.rollback()
        else:
            pass