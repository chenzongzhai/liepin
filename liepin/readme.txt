
# scrapy 官方文档
http://scrapy-chs.readthedocs.io/zh_CN/latest/intro/tutorial.html

# scrapy 项目参考资料
http://www.wtoutiao.com/a/3063656.html

# scrapy 写数据库资料
http://www.sharejs.com/codes/python/8392
https://www.douban.com/group/topic/71578175/

# scrapy 更改下载器中间键，设置代理ip
http://blog.csdn.net/yelbosh/article/details/21542073

#　mysql数据库建表语句
CREATE TABLE `liepin` (
   `id` int(4) NOT NULL auto_increment,
   `url` varchar(100) NOT NULL,
   `code_md5` varchar(32) NOT NULL,
   `name` varchar(100) NOT NULL,
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
