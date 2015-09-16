# -*- coding: utf-8 -*-
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
class PyConnect(object):
    
    def __init__(self):
        #conn 类型<class 'pymongo.connection.Connection'>
        try:
            conn = MongoClient('123.57.221.18', 27017)
            self.Mongodb = conn["fitgo"]
            self.Mongodb.authenticate('fitgoUser','fitgo2015')
        except  Exception,e:
            print 'connect to %s:%s fail' %(host, port)
            exit(0)
        plan = self.Mongodb.Plan.find({},{'content':1})
        print plan
        for i in plan:
            print i['content']#['1']

    # def __del__(self):
    #     self.conn.close()

    # def use(self, dbname):
    #     # 这种[]获取方式同样适用于shell,下面的collection也一样
    #     #db 类型<class 'pymongo.database.Database'>
    #     self.db = self.conn[dbname]

    # def setCollection(self, collection):
    #     if not self.db:
    #         print 'don\'t assign database'
    #         exit(0)
    #     else:
    #         self.coll = self.db[collection]

    # def find(self, query = {}):
    #     #注意这里query是dict类型
    #     if type(query) is not dict:
    #         print 'the type of query isn\'t dict'
    #         exit(0)
    #     try:
    #         #result类型<class 'pymongo.cursor.Cursor'>
    #         if not self.coll:
    #             print 'don\'t assign collection'
    #         else:
    #             result = self.coll.find(query)
    #     except NameError:
    #         print 'some fields name are wrong in ',query
    #         exit(0)
    #     return result

    # def insert(self, data):
    #     if type(data) is not dict:
    #         print 'the type of insert data isn\'t dict'
    #         exit(0)
    #     #insert会返回新插入数据的_id
    #     self.coll.insert(data)

    # def remove(self, data):
    #     if type(data) is not dict:
    #         print 'the type of remove data isn\'t dict'
    #         exit(0)
    #     #remove无返回值
    #     self.coll.remove(data)

    # def update(self, data, setdata):
    #     if type(data) is not dict or type(setdata) is not dict:
    #         print 'the type of update and data isn\'t dict'
    #         exit(0)
    #     #update无返回值
    #     self.coll.update(data,{'$set':setdata})

if __name__ == '__main__':
	a = PyConnect()
	# plan = self.Mongodb().Plan.find({})
	# for i in plan:
	# 	print i
    # connect = PyConnect('123.57.221.18', 27017)
    # connect.use('test_for_new')
    # connect.setCollection('collection1')
    # connect.insert({'a':10, 'b':1})
    # result = connect.find()
    # connect.update({'a':10, 'b':1}, {'b':10})
    # #x也是dict类型，非常好
    # for x in result:
    #     if 'c' in x:
    #         print x['_id'], x['a'], x['b'], x['c']
    #     else:
    #         print x['_id'], x['a'], x['b']
    # connect.remove({'a':10})