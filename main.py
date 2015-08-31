#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@date  :2015-3-from
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.web
import os

from tornado.options import define, options
from UI_moudles.UI_moudle import *

define("port", default=3000, help="run on the given port", type=int)
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',MainHandler),
            ]
        settings = dict(
            cookie_secret="7CA71A57B571B5AEAC5E64C6042415DE",
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            ui_modules={'header':HeaderMoudle,'footer':FooterMoudle},
            # static_url_prefix = os.path.join(os.path.dirname(__file__), '/images/'),
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('body.html')


if __name__ == "__main__":
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
