# 腾讯(鹅厂)招聘爬虫

想了解下今年的互联网招聘行情以及之后的趋势，鹅厂是一个不错的数据源。网站看得太疼苦，萌生了把数据全部拉下来再分析的想法。于是去同性交友网站翻到了zi-ming基于Scrapy的[小项目](https://github.com/zi-ming/tencentRuleSpider)， 在此基础上花半个小时看了下Scrapy并做了一点优化，可以拉取到所有社招的**职位名称、职位类别、招聘人数、工作地点、发布时间、详细链接、工作职责、工作要求。**

用法：python3.5+(其它环境没试)运行start.py，结束后会在主目录生成一个.csv文件。

