# 用到的库
scrapy 1.0.5

DBUtils-1.1-py2.7.egg

MySQL_python-1.2.5-py2.7.egg-info

MySQLdb

# liepin
scrapy爬取猎聘网招聘信息

由scrapy框架实现的可以爬取猎聘网全站招聘信息，并将信息提取(网站地址，职位信息，公司信息，薪资要求)保存到MySQL数据库中，支持更新。

爬取入口地址，爬取规则，数据库配置信息统一写在config.py文件中

启动程序需要先配置好MySQL数据库信息，创建对应表，建表语句参考：

CREATE TABLE `liepin` (

   `id` int(4) NOT NULL auto_increment,
   
   `url` varchar(100) NOT NULL,
   
   `code_md5` varchar(32) NOT NULL,
   
   `name` varchar(100) NOT NULL,
   
   `company_name` varchar(200) default NULL,
   
   `publish_time` date default NULL,
   
   `create_time` timestamp NOT NULL,
   
   `requires` varchar(100) default NULL,
   
   `pay` varchar(50) default NULL,
   
   `company_size` varchar(30) default NULL,
   
   `company_address` varchar(200) default NULL,
   
   `company_type` varchar(50) default NULL,
   
   PRIMARY KEY  (`id`),
   
   UNIQUE KEY `code_md5` (`code_md5`)
   
) ENGINE=InnoDB AUTO_INCREMENT=390 DEFAULT CHARSET=utf8;

启动命令：scrapy crawl liepin

项目中log还有些问题，应该有更好的写法，之后会项目中添加download中间件，itemloder。

个人感觉scrapy跟django很像

# 参考资料：

scrapy 官方文档
http://scrapy-chs.readthedocs.io/zh_CN/latest/intro/tutorial.html

scrapy 项目参考资料
http://www.wtoutiao.com/a/3063656.html

scrapy 写数据库资料
http://www.sharejs.com/codes/python/8392
https://www.douban.com/group/topic/71578175/

scrapy 更改下载器中间键，设置代理ip
http://blog.csdn.net/yelbosh/article/details/21542073

......
