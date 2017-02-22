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
        self.hDB.drop_all_table()
        self.hDB.create_all_table()
       '''
        # 清空各表
        self.hDB.delete_all_table()

    def __del__(self):
        self.hDB.close_db()

    def process_item(self, item, spider):
        self.item_count+=1
        print(item)
        print("第%d个Item" % self.item_count)
        self.hDB.insert_goods_item(item['goods_id'], item['title'], item['page_id'],item['logo'],item['price']
                             ,item['brand'],item['goods_des'])

        self.hDB.insert_page_goods(item['goods_id'], item['page_id'])

        self.hDB.insert_goods_img(item['goods_id'], "zoom_b1", item['pic_zoom_b1'])
        self.hDB.insert_goods_img(item['goods_id'], "zoom_b2", item['pic_zoom_b2'])
        self.hDB.insert_goods_img(item['goods_id'], "zoom_m", item['pic_zoom_m'])
        self.hDB.insert_goods_img(item['goods_id'], "img_des", item['pic_des'])

        self.hDB.insert_goods_attr(item['goods_id'], item['params_name'],item['params_val'])





