import tornado.web
import tornado.gen
from Base_Handler import BaseHandler
from ..databases.tables import UsersCache

# class User_Handler(BaseHandler):


	# uid = Column(Integer,primary_key=True)
	# name = Column(VARCHAR(64),nullable=False)
	# student_card = Column(VARCHAR(64),nullable=False)
	# student_id = Column(Integer,nullable=False)
	# gender = Column(VARCHAR(64))
	# user_name = Column(VARCHAR(64))
	# school = Column(VARCHAR(64))
	# campus = Column(VARCHAR(64))
	# password = Column(VARCHAR(64))
	# info_email = Column(VARCHAR(64))
	# info_phone = Column(VARCHAR(64))
	# portrait = Column(VARCHAR(64))

	name = "tom"
	




	me = UsersCache(name)
	db.session.add(me)
    db.session.commit()