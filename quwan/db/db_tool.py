import sqlite3

class DBImpl(object):
    def open_db(self):
        self.conn = sqlite3.connect("./quwan/db/quwan_data.db")
        print ("Opened database successfully")

    def close_db(self):
        self.conn.close()


    def exesql(self, sql):
        self.conn.execute(sql)


    def create_goods_table(self): #商品基本信息表
        self.conn.execute('''
        create table goods_base(
       id             char(50)  PRIMARY KEY     NOT NULL,
       name       char(256) NOT  NULL ,
       page_idx       char(50)    NOT NULL,
       logo          char(256)    ,
       price        REAL NOT  NULL ,
       brand         char(100) NOT NULL ,
       description  TEXT);
        ''')
        print("create table success: 商品基本信息表")

    def delete_goods_base_tab(self):
        self.__delete_table("goods_base")

    def create_pageidx_table(self): #页面索引表
        self.conn.execute('''
                create table page_goods(
               page_id        char(50)  PRIMARY KEY     NOT NULL,
               goods_id       char(50) NOT  NULL);
                ''')
        print("create table success: 页面--商品关联表")
    def delete_page_goods_tab(self):
        self.__delete_table("page_goods")


    def create_img_table(self): #图片表
        self.conn.execute('''
            create table goods_img(
           goods_id             char(50)  PRIMARY KEY     NOT NULL,
           pic_type               char(20) NOT  NULL ,
           url       char(256)    NOT NULL,
           idx      INT NOT NULL
           );
            ''')
        print("create table success: 商品--图片表")
    def delete_img_tab(self):
        self.__delete_table("goods_img")

    def create_attr_table(self): #商品属性表
        self.conn.execute('''
            create table goods_attr(
           goods_id             char(50)  PRIMARY KEY     NOT NULL,
           attr_name               char(50) NOT  NULL ,
           attr_value       char(50)    NOT NULL
           );
            ''')
        print("create table success: 商品--属性表"  )
    def delete_attr_tab(self):
        self.__delete_table("goods_attr")

    def drop_table(self, table_name):
        sql = "drop table " + table_name + ";"
        print("drop table success: %s" % table_name)

    def __delete_table(self, table_name):
        sql = "delete form" + table_name + ";"
        self.conn.execute(sql)
        print("delete table %s success!" % table_name)

