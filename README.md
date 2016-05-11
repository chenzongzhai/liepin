# 用到的库
scrapy 1.0.5

DBUtils-1.1-py2.7.egg

MySQL_python-1.2.5-py2.7.egg-info

MySQLdb

# liepin
scrapy爬取猎聘网招聘信息

由scrapy框架实现的可以爬取猎聘网全站招聘信息，并将信息提取保存到MySQL数据库中，支持更新。

爬取入口地址，爬取规则，数据库配置信息统一写在config.py文件中

启动程序需要先配置好MySQL数据库信息，创建对应表，建表语句参考：

CREATE TABLE `liepin` (

   `id` int(4) NOT NULL auto_increment,
   
   `url` varchar(100) NOT NULL,
   
   `code_md5` varchar(32) NOT NULL,
   
   `name` varchar(00) NOT NULL,
   
   `company_name` varchar(200) default NULL,
   
   `publish_time` date default NULL,
   
   `create_time` timestamp default NULL,
   
   `requires` varchar(100) default NULL,
   
   `pay` varchar(50) default NULL,
   
   `company_size` varchar(30) default NULL,
   
   `company_address` varchar(200) default NULL,
   
   `company_type` varchar(50) default NULL,
   
   PRIMARY KEY  (`id`),
   
   UNIQUE KEY `code_md5` (`code_md5`)
   
 ) ENGINE=InnoDB AUTO_INCREMENT=390 DEFAULT CHARSET=utf8;

启动命令：scrapy crawl lipin
