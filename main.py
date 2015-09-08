
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
from mod.auth.Login_Handler import LoginHandler
from mod.auth.Logout_Handler import LogoutHandler
from mod.auth.Register_Handler import RegisterHandler,VerifyHandler
from mod.auth.Base_Handler import BaseHandler
from mod.auth.Password_Handler import PasswordHandler

from mod.user.UserInfo_Handler import UserinfoHandler
from mod.user.Usertopic_Handler import UsertopicHandler
from mod.index.index import IndexHandler
from mod.activity.ActivityPage_Handler import ActivityPageHandler
from mod.activity.CreateActivity_Handler import CreateActivityHandler
from mod.activity.SearchActivity_Handler import SearchActivityHandler
from mod.invite.InvitePage_Handler import InvitePageHandler
from mod.discover.DiscoverPage_Handler import DiscoverPageHandler
from mod.discover.CreateState_Handler import CreateStateHandler
from mod.discover.AddFriend_Handler import AddFriendHandler
from mod.discover.SearchFriend_Handler import SearchFriendHandler
from mod.discover.SearchState_Handler import SearchStateHandler
from mod.plans.Plans_Handler import PlansHandler
define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',IndexHandler),
            (r'/body',BodyHandler),
            (r'/auth/login',LoginHandler),
            (r'/auth/logout', LogoutHandler),
            #(r'/userinfo',WatchUserHandler),
            (r'/user/userinfo/(\d+)',UserinfoHandler),
            (r'/user/usertopic/(\d+)',UsertopicHandler),
            (r'/auth/register/verify',VerifyHandler),
            (r'/auth/register',RegisterHandler),
            (r'/auth/password',PasswordHandler),
            (r'/test',TestHandler),
            (r'/invite/user_page',InvitePageHandler),
            (r'/activity',ActivityPageHandler),
            (r'/activity/create',CreateActivityHandler),
            (r'/activity/search',SearchActivityHandler),
            (r'/discover/discover_page',DiscoverPageHandler),
            (r'/discover/add',AddFriendHandler),
            (r'/discover/search/friends',SearchFriendHandler),
            (r'/discover/create',CreateStateHandler),
            (r'/discover/search/state',SearchStateHandler),
            (r'/plans',PlansHandler)
            ]
        settings = dict(
            cookie_secret="7CA71A57B571B5AEAC5E64C6042415DE",
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            auth_path=os.path.join(os.path.dirname(__file__),'auth'),
            discover_path=os.path.join(os.path.dirname(__file__),'discover'),
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

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html')
        
if __name__ == "__main__":
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
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
from mod.auth.Login_Handler import LoginHandler
from mod.auth.Logout_Handler import LogoutHandler
from mod.auth.Register_Handler import RegisterHandler,VerifyHandler
from mod.auth.Base_Handler import BaseHandler
from mod.auth.Password_Handler import PasswordHandler

from mod.user.UserInfo_Handler import UserinfoHandler
from mod.user.Usertopic_Handler import UsertopicHandler
from mod.user.UserPage_Handler import UserPageHandler

from mod.plans.Lookplans_Handler import LookplansHandler
from mod.plans.Star_Handler import StarHandler
from mod.plans.Plans_Handler import PlansHandler


from mod.index.index import IndexHandler

from mod.activity.ActivityPage_Handler import ActivityPageHandler
from mod.activity.CreateActivity_Handler import CreateActivityHandler
from mod.activity.SearchActivity_Handler import SearchActivityHandler
from mod.activity.AddActivity_Handler import AddActivityHandler

from mod.invite.InvitePage_Handler import InvitePageHandler

from mod.discover.DiscoverPage_Handler import DiscoverPageHandler
from mod.discover.CreateState_Handler import CreateStateHandler
from mod.discover.AddFriend_Handler import AddFriendHandler
from mod.discover.SearchFriend_Handler import SearchFriendHandler
from mod.discover.SearchState_Handler import SearchStateHandler

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',IndexHandler),
            (r'/body',BodyHandler),
            (r'/auth/login',LoginHandler),
            (r'/auth/logout', LogoutHandler),

            (r'/plans/lookplans/(\d+)',LookplansHandler),
            (r'/plans/plans/(\d+)',PlansHandler),
            (r'/plans/star/(\d+)',StarHandler),

            (r'/user/userinfo/(\d+)',UserinfoHandler),
            (r'/user/usertopic/(\d+)',UsertopicHandler),
            (r'/user/userpage/(\d+)',UserPageHandler),
            (r'/auth/register/verify',VerifyHandler),
            (r'/auth/register',RegisterHandler),
            (r'/auth/password',PasswordHandler),
            (r'/test',TestHandler),
            (r'/invite/user_page',InvitePageHandler),
            (r'/activity',ActivityPageHandler),
            (r'/activity/create',CreateActivityHandler),
            (r'/activity/search',SearchActivityHandler),
            (r'/activity/add',AddActivityHandler),
            (r'/discover/discover_page',DiscoverPageHandler),
            (r'/discover/add',AddFriendHandler),
            (r'/discover/search/friends',SearchFriendHandler),
            (r'/discover/create',CreateStateHandler),
            (r'/discover/search/state',SearchStateHandler)
            ]
        settings = dict(
            cookie_secret="7CA71A57B571B5AEAC5E64C6042415DE",
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            auth_path=os.path.join(os.path.dirname(__file__),'auth'),
            discover_path=os.path.join(os.path.dirname(__file__),'discover'),
            activity_path=os.path.join(os.path.dirname(__file__),'activity'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            ui_modules={'header':HeaderMoudle,'footer':FooterMoudle},
            # xsrf_cookies=True,
            login_url="/auth/login",
            # static_url_prefix = os.path.join(os.path.dirname(__file__), '/images/'),
            debug=True
            # "lohin_url":"/auth/LoginHandler"
            
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))
class BodyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('body.html')

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html')
        
if __name__ == "__main__":
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
