# -*- coding: utf-8 -*-
#@date  :2015-3-from

import tornado.web

class HeaderMoudle(tornado.web.UIModule):
    def render(self):
        return self.render_string('header.html')

class FooterMoudle(tornado.web.UIModule):
    def render(self):
        return self.render_string('footer.html')


