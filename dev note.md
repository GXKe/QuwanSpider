# Scrapy 初体验

- scrapy startproject   *project_name*  创建工程

- scrapy genspider -t basic  *spider_name* *website.com* 以basic模版创建爬虫

- ROBOTSTXT_OBEY = False  不遵守Robots协议

- Item 添加字段

- 添加pipeline用于Item处理（输出到屏幕/数据/json）

- 配置pipeline  **dangdang.pipelines.DangdangPipeline&#39;: 300    **

- 添加爬取逻辑 ：    def parse(self, response):

- scrapy crawl *spider_name*  —nolog 启动爬虫



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
	/a[@href] 专题详情页link (存在不完整连接)
	/a/img[@onerror="imgerror(event)"][@src] 专题头像link

	
```

235x235小方块

```
    brick col1 commodity bestlikes masonry-brick 商品定位
	
    //div[@class=='brick col2 masonry-brick'] 商品定位
	/a[@href] 商品详情页link (存在不完整连接)
	/a[@title] 名称
	/a/img[@onerror="imgerror(event)"][@src] 商品头像link
	/dl/dd/a[@href]  商品详情页link (存在不完整连接)
	/dl/dd/a[@title]  名称
	/dl/dd/span 价格
	
```


滚动交互区域
    `brick col1 userActive`

一键回顶部
`goTop_box`



### 商品详情页分析
```

//div[@class='informations'] 缩略图特效区域
//div[@class='informations']//div[@="itempic"]/a/img[@src] 多个大图
//div[@class='informations']//ul[@class="pic_index"]/li/img[@src]   对应多个小图

//div[@id="paykey_new"]//ul/li/dl/dt  品牌


//div[@class="product_mess"] //商品信息
//div[@class="mess_box"] //商品信息
//div[@class="box details"] //商品图片详情,多图组成

```


### 需要考虑扩展的部分
- 品牌
- 好评指数
- 库存&到货通知
- 喜欢
- 放上自己的微信二维码
- 分享链接可以考虑是否添加上

### 问题点
- 首页--详情，产品ID如何匹配？
- 数据库，手动建库还是对象映射,json?
- 缩略图特效支持