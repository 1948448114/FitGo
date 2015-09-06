# -*- coding: utf-8 -*-
#!/usr/bin/env python
#@date  :2015-3-from
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
from tornado.options import define, options

from sqlalchemy.orm import scoped_session, sessionmaker
from mod.databases.db import engine
from UI_moudles.UI_moudle import *
from mod.auth.Login_Handler import LoginHandler,LogoutHandler
from mod.auth.Base_Handler import BaseHandler
from mod.index.index import IndexHandler
from mod.user.Userinfo_Handler import UserinfoHandler
from mod.user.Usertopic_Handler import UsertopicHandler

from mod.databases.tables import UsersCache 
from mod.databases.tables import User_tagCache


define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',IndexHandler),
            (r'/body',BodyHandler),
            (r'/auth/login',LoginHandler),
            (r'/auth/logout', LogoutHandler),
            (r'/userinfo',WatchUserHandler),
            (r'/user/userinfo/(\d+)',UserinfoHandler),
            (r'/user/usertopic/(\d+)',UsertopicHandler),
            ]
        settings = dict(
            cookie_secret="<7CA71A57B571B5AEAC5E64C6042415DE></7CA71A57B571B5AEAC5E64C6042415DE>",
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            auth_path=os.path.join(os.path.dirname(__file__),'auth'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            ui_modules={'header':HeaderMoudle,'footer':FooterMoudle},
            # xsrf_cookies=True,
            login_url="/auth/login",
            # static_url_prefix = os.path.join(os.path.dirname(__file__), '/images/'),
            debug=True,
            # "lohin_url":"/auth/LoginHandler"
            
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))
class BodyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('body.html')



class WatchUserHandler(BaseHandler):
    """docstring for WatchUser_handler"""

    @property
    def db(self):
        return self.application.db


    def on_finish(self):
        self.db.close()


    def get(self):
        # 获取id
        # uid = self.get_argument('id')
        uid = 1

        person = self.db.query(UsersCache).filter(UsersCache.uid == uid).one()

        
        
        uid = person.uid
        name = person.name
        student_card = person.student_card
        student_id = person.student_id
        gender = person.gender
        user_name = person.user_name
        school = person.school
        campus = person.campus
        password = person.password
        info_email = person.info_email
        info_phone = person.info_phone
        portrait = person.portrait


        tags = self.db.query(User_tagCache).filter(User_tagCache.uid == uid).one()

        user_enjoyment = tags.user_enjoyment
        user_join_times = tags.user_join_times
        user_score = tags.user_score
        user_join_event = tags.user_join_event

        json = "{uid:"+str(uid)+",name:"+str(name)+",student_card:"+str(student_card)+",student_id:"+str(student_id)+",gender:"+str(gender)+",user_name:"+str(user_name)+",school:"+str(school)+",campus:"+str(campus)+",info_email:"+str(info_email)+",info_phone:"+str(info_phone)+",portrait:"+str(portrait)+",user_enjoyment:"+str(user_enjoyment)+",user_join_times:"+str(user_join_times)+",user_score:"+str(user_score)+",user_join_event:"+str(user_join_event)+"}"

        # json = "{totalPorperty:" + dt1.Rows[0]["totalPorperty"].ToString() + ",root:" + json + "}"

        self.render("userinfo.html",json=json)
        # self.write(json) 







if __name__ == "__main__":
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
