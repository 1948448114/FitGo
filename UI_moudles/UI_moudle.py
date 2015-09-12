# -*- coding: utf-8 -*-
#@date  :2015-3-from

import tornado.web

class HeaderMoudle(tornado.web.UIModule):
    def render(self):
        return self.render_string('header.html')

class FooterMoudle(tornado.web.UIModule):
    def render(self):
        return self.render_string('footer.html')
class activity_itemMoudle(tornado.web.UIModule):
    def render(self,content):
        return self.render_string('activity_item.html',content=content)
class act_join_peopleMoudle(tornado.web.UIModule):
    def render(self,content):
        return self.render_string('act_join_people.html',content=content)
class plan_itemMoudle(tornado.web.UIModule):
	def render(self,content1,content2):
		return self.render_string('plan_items.html',content=content1,content2=content2)

class DiscoverStateMoudle(tornado.web.UIModule):
    def render(self,content):
        return self.render_string('discover_state.html',content=content)
        
class DiscoverFriendMoudle(tornado.web.UIModule):
    def render(self,content):
        return self.render_string('discover_friend.html',content=content)