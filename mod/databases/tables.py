#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, VARCHAR,ForeignKey
from db import engine,Base

class UsersCache(Base):
	__tablename__ = 'Users'

	uid = Column(Integer,primary_key=True)
	name = Column(VARCHAR(64),nullable=True)
	student_card = Column(VARCHAR(64),nullable=True)
	student_id = Column(Integer,nullable=True)
	gender = Column(VARCHAR(64))
	user_name = Column(VARCHAR(64))
	school = Column(VARCHAR(64))
	campus = Column(VARCHAR(64))
	password = Column(VARCHAR(64))
	info_email = Column(VARCHAR(64))
	info_phone = Column(VARCHAR(64))
	portrait = Column(VARCHAR(64))
class CookieCache(Base):
	__tablename__ = "Cookie"

	id = Column(Integer,primary_key=True)
	uid = Column(Integer)
	cookie = Column(VARCHAR(64))
class PlansCache(Base):
	__tablename__ = 'Plans'

	plan_id = Column(Integer,primary_key=True)
	uid = Column(Integer)
	create_time = Column(VARCHAR(64),nullable=False)
	start_time = Column(VARCHAR(64))
	end_time = Column(VARCHAR(64))
	fit_location = Column(VARCHAR(64))
	fit_item = Column(VARCHAR(64))
	remark = Column(VARCHAR(64))
	grader = Column(VARCHAR(64))

class User_tagCache(Base):
	__tablename__ = 'User_tag'

	uid = Column(Integer,primary_key=True)
	user_enjoyment = Column(VARCHAR(64))
	user_join_times = Column(Integer)
	user_score = Column(VARCHAR(64))
	user_join_event = Column(VARCHAR(64))

class ActCache(Base):
	__tablename__ = 'Act'

	act_id = Column(Integer,primary_key=True)
	uid = Column(Integer)
	start_time = Column(VARCHAR(64))
	end_time = Column(VARCHAR(64))
	act_style = Column(VARCHAR(64))
	act_people_num = Column(Integer)
	act_detail = Column(VARCHAR(64))
	act_address = Column(VARCHAR(64))
	act_join_way = Column(VARCHAR(64))
	act_join_uid = Column(Integer)

class TopicsCache(Base):
	__tablename__ = 'Topics'

	topic_id = Column(Integer,primary_key=True)
	topic_content = Column(VARCHAR(64))
	topic_pic = Column(VARCHAR(64))
	topic_title = Column(VARCHAR(64))
	topic_starers = Column(Integer)