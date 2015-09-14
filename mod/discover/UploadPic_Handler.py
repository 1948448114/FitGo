#!/usr/bin/python
#-*- encoding:utf-8 -*-
import tornado.ioloop
import tornado.web
import shutil
import os
from mod.auth.Base_Handler import BaseHandler
#/discover/create/state/pic
class UploadPicHandler(BaseHandler):
    def get(self):
        # pass
        self.render("upload_pic.html",user=self.current_user)
 
    def post(self):
        upload_path=os.path.join(os.path.dirname('mod'),'static/picture')  #文件的暂存路径
        file_metas=self.request.files['file']    #提取表单中‘name’为‘file’的文件元数据
        if file_metas:
            retjson = {'code':200,'content':'picture upload success!'}
            for meta in file_metas:
                filename=meta['filename']
                # newname=i.replace(filename,'123')
                # os.rename(filename,newname)
                filepath=os.path.join(upload_path,filename)
                print filepath,type(meta)
                with open(filepath,'wb') as up:      #有些文件需要已二进制的形式存储，实际中可以更改
                    up.write(meta['body'])
            retjson['content'] = filepath
            print filepath
        else:
            retjson = {'code':400,'content':'failed to upload picture'}

        self.write(retjson)
 