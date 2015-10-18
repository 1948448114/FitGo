# -*- coding: utf-8 -*-
DB_HOST = '115.28.27.150'
DB_USER = 'fitgouser'
DB_PWD = 'fitgo2015'
DB_NAME = 'fitgo'



from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() #create Base lei
engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8' %
                       (DB_USER, DB_PWD, DB_HOST, DB_NAME),
                     encoding='utf-8', echo=False,
                       pool_size=100, pool_recycle=10)
