# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from quwan.db.db_tool import DBImpl


class QuwanPipeline(object):
    item_count = 0
    def __init__(self):
        self.hDB = DBImpl()
        self.hDB.open_db()
'''
        #调用一次:建表
        self.hDB.create_attr_table()
        self.hDB.create_goods_table()
        self.hDB.create_img_table()
        self.hDB.create_pageidx_table()
'''
    def __del__(self):
        self.hDB.close_db()

    def process_item(self, item, spider):
        self.item_count+=1
        print(item)
        print("第%d个Item" % self.item_count)
