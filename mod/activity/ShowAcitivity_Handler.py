import tornado.web
import tornado.gen
from mod.auth.Base_Handler import BaseHandler
from ..databases.tables import ActCache
import traceback
import time
#/activity/
class ShowAcitivityHandler(tornado.web.RequestHandler):
	def post(self):#查看活动
		