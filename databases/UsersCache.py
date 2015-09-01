#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, VARCHAR,ForeignKey
from db import engine,Base

class UsersCache(Base):
	__tablename__ = 'Users'

	uid = Column(Integer,primary_key=True)
	name = Column(VARCHAR(64))
	student_card = Column(VARCHAR(64))
	student_id = Column(Integer)
	gender = Column(VARCHAR(64))
	user_name = Column(VARCHAR(64))
	school = Column(VARCHAR(64))
	campus = Column(VARCHAR(64))
	password = Column(VARCHAR(64))
	info_email = Column(VARCHAR(64))
	info_phone = Column(VARCHAR(64))
	portrait = Column(VARCHAR(64))
