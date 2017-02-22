#开发笔记
## Scrapy 初体验

- scrapy startproject   *project_name*  创建工程

- scrapy genspider -t basic  *spider_name* *website.com* 以basic模版创建爬虫

- ROBOTSTXT_OBEY = False  不遵守Robots协议

- Item 添加字段

- 添加pipeline用于Item处理（输出到屏幕/数据/json）

- 配置pipeline  **dangdang.pipelines.DangdangPipeline&#39;: 300    **

- 添加爬取逻辑 ：    def parse(self, response):

- scrapy crawl *spider_name*  —nolog 启动爬虫

#### PyCharm中启动爬虫调试
命令行执行 `scrapy crawler spider`启动爬虫，其实与下面指令是一样的：
`python C:\Python34\Lib\site-packages\scrapy\cmdline.py crawl spider_name`
的效果是一样的


这样只需要在pycharm中的Run下Edit Configurations...中做运行配置即可：
Script: `C:\Python34\Lib\site-packages\scrapy\cmdline.py`
Script parameters: `crawl spider_name`

#### XPath
```
/div[@attr='xxxx']  选择属性为xxxx的div标签
a/@title.extract() 输出a标签内的title属性值
a/text() 取标签文本

print ("title : " + p.xpath('dl/dd/a/@title').extract()) 
print("link : " + p.xpath('dl/dd/a/@href').extract())
print("price : " + p.xpath('dl/dd/span/text()').extract())  取标签文本
print("logo : " + p.xpath('a/img[@onerror="imgerror(event)"]/@src').extract())
print("link : " + p.xpath('dl/dd/a/@href').extract())
```
##趣玩网

### 创建工程
```
scrapy startproject quwan
scrapy genspider -t basic QuwanSpider quwan.com
ROBOTSTXT_OBEY = False
```

### 首页html分析规律
480x480大方块
```
    brick col2 masonry-brick 专题定位
    
    //div[@class=='brick col2 masonry-brick'] 专题定位
    /a/@href 专题详情页link (存在不完整连接)
    /a/img[@onerror="imgerror(event)"]/@src 专题头像link

    
```

235x235小方块

```
    brick col1 commodity bestlikes masonry-brick 商品定位
    
    //div[@class='brick col1 commodity bestlikes masonry-brick'] 商品定位
    /a/@href 商品详情页link (存在不完整连接)
    /a/@title 名称
    /a/img[@onerror="imgerror(event)"]/@src 商品头像link
    /dl/dd/a/@href  商品详情页link (存在不完整连接)
    /dl/dd/a/@title  名称
    /dl/dd/span.text() 价格
    
```


滚动交互区域
    `brick col1 userActive`

一键回顶部
`goTop_box`



### 商品详情页分析及提取
```
缩略图特效区域
//a[@class="cloud-zoom"]/@href 缩略大图1
//a[@class="cloud-zoom"]/img/@src 缩略大图2
//ul[@class="pic_index"]/li[@class="pic_li"]/img/@src 缩略小图

//div[@id="paykey_new"]//ul/li/dl/dt  品牌


//div[@class="product_mess"] //商品信息
//div[@class="mess_box"] //商品信息
//div[@class="box details"]/p/img/@src  商品图片详情,多图组成
//div[@class="gn_decri"]/p/text()  商品介绍文本

```

### 商品Item对象字段定义
```
class QuwanItem(scrapy.Item):
  # define the fields for your item here like:
 # name = scrapy.Field()  
 goods_id = scrapy.Field()   #商品id
  page_id = scrapy.Field()    #商品索引页
  logo = scrapy.Field()       #商品列表logo
  price = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()  #品牌

  pic_zoom_b1 = scrapy.Field() #缩略大图1
  pic_zoom_b2 = scrapy.Field() #缩略大图2
  pic_zoom_m = scrapy.Field()  #缩略小图

  pic_des  = scrapy.Field() #商品详情图
  goods_des = scrapy.Field() #商品文本简介

  params_name = scrapy.Field()    #参数
  params_val = scrapy.Field()
```


> **坑爹的item**
item.goods_id = "xxxx"  不能这样访问
item['goods_id'] = "xxxx" 非得这样访问

``` 
yield item 返回item对象

安装加工管道逐个处理item
ITEM_PIPELINES = {
    'quwan.pipelines.QuwanPipeline': 300,
}
```

### DB 数据持久化
[使用SQLAlchemy教程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0014021031294178f993c85204e4d1b81ab032070641ce5000)

###### 页面表
>页面id， 商品id

###### 图片表
>商品id， 图片顺序号， 图片链接, 图片类型（logo，缩放图，产品详情图）

###### 商品信息表
> 商品id，价格、名称、参数、赞数量


### 需要考虑扩展的部分
- 品牌
- 好评指数
- 库存&到货通知
- 点赞喜欢
- 放上自己的微信二维码
- 分享链接可以考虑是否添加上

### 问题点
- 首页--详情，产品ID如何匹配？
- 数据库，手动建库还是对象映射,json?
- 缩略图特效支持
- Scrapy 如何多线程