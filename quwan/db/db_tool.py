import sqlite3

class DBImpl(object):
    def open_db(self):
        self.conn = sqlite3.connect("./quwan/db/quwan_data.db")
        print ("Opened database successfully")

    def close_db(self):
        self.conn.close()


    def exesql(self, sql):
        self.conn.execute(sql)

    def delete_all_table(self):
        self.delete_attr_tab()
        self.delete_goods_base_tab()
        self.delete_img_tab()
        self.delete_page_goods_tab()
        self.conn.commit()
        print("delete all table success !")

    def drop_all_table(self):
        self.drop_table("goods_base")
        self.drop_table("page_goods")
        self.drop_table("goods_img")
        self.drop_table("goods_attr")
        self.conn.commit()
        print("drop all table success !")

    def create_all_table(self):
        self.create_img_table()
        self.create_pageidx_table()
        self.create_goods_table()
        self.create_attr_table()
        self.conn.commit()
        print ("create all table success !")


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

    def insert_goods_item(self, id, name, page, logo, price, brand, des):
        price = price.replace('¥', '')
        sql = "INSERT INTO goods_base VALUES (" + '\'' + id +"\',\'" + name +"\',\'" + page  +"\',\'" + logo +"\'," + price +",\'" +brand +"\',\'" +des +"\');"
        self.conn.execute(sql)
        self.conn.commit()
        print(sql)

    def delete_goods_base_tab(self):
        self.__delete_table("goods_base")


    def create_pageidx_table(self): #页面索引表
        self.conn.execute('''
                create table page_goods(
               page_id        char(50)  NOT NULL,
               page_title     char(100) NOT NULL,
               goods_id       char(50) NOT  NULL);
                ''')
        print("create table success: 页面--商品关联表")

    def insert_page_goods(self, page_id, page_title,  goods_id):
        sql = "INSERT INTO page_goods VALUES (" + '\'' + page_id +"\',\'"  + page_title +"\',\'" + goods_id +"\');"
        self.conn.execute(sql)
        self.conn.commit()
        print(sql)

    def delete_page_goods_tab(self):
        self.__delete_table("page_goods")



    def create_img_table(self): #图片表
        self.conn.execute('''
            create table goods_img(
           goods_id             char(50)  NOT NULL,
           pic_type               char(20) NOT  NULL ,
           url       char(256)    NOT NULL,
           idx      INT NOT NULL
           );
            ''')
        print("create table success: 商品--图片表")

    def insert_goods_img(self, goods_id, type, url_list):
        idx = 0
        for url in url_list:
            sql = "INSERT INTO goods_img VALUES (" + '\'' \
                  + goods_id +"\',\'"\
                  + type +"\',\'" \
                  + url + "\'," \
                  + str(idx) +");"
            idx +=1
            self.conn.execute(sql)
            print(sql)

        self.conn.commit()

    def delete_img_tab(self):
        self.__delete_table("goods_img")

    def create_attr_table(self): #商品属性表
        self.conn.execute('''
            create table goods_attr(
           goods_id             char(50)    NOT NULL,
           attr_name               char(50) NOT  NULL ,
           attr_value       char(50)    NOT NULL
           );
            ''')
        print("create table success: 商品--属性表"  )

    def insert_goods_attr(self, goods_id, attr_name_list, attr_value_list):

        listlen = len(attr_name_list)
        if (listlen > len(attr_value_list)):
            listlen = len(attr_value_list)

        for idx in range(listlen):
            sql = "INSERT INTO goods_attr VALUES (" + '\'' \
                  + goods_id +"\',\'"\
                  + attr_name_list[idx] +"\',\'" \
                  + attr_value_list[idx]\
                   + "\');"
            self.conn.execute(sql)
            print(sql)
        self.conn.commit()

    def delete_attr_tab(self):
        self.__delete_table("goods_attr")

    def drop_table(self, table_name):
        sql = "drop table " + table_name + ";"
        self.conn.execute(sql)
        print("drop table success: %s" % table_name)

    def __delete_table(self, table_name):
        sql = "delete from " + table_name + ";"
        self.conn.execute(sql)
        print("delete table %s success!" % table_name)

