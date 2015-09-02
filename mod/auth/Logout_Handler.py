
#/auth/logout
class LogoutHandler(tornado.web.RequestHandler):
	def delete(self):#用户登出，删除cookie
		pass