# sinaSpider/settings.py

BOT_NAME = 'sinaSpider'
SPIDER_MODULES = ['sinaSpider.spiders']
NEWSPIDER_MODULE = 'sinaSpider.spiders'

# 1. 关闭机器人协议，确保能爬取
ROBOTSTXT_OBEY = False

# 2. 极大提高并发请求数 (默认 16，改为 100 以实现快速爬取)
CONCURRENT_REQUESTS = 100

# 3. 将下载延迟设为 0，取消请求间隔
DOWNLOAD_DELAY = 0

# 4. 提高单域名的并发量
CONCURRENT_REQUESTS_PER_DOMAIN = 50
CONCURRENT_REQUESTS_PER_IP = 50

# 5. 关闭 Cookies 以节省带宽和计算
COOKIES_ENABLED = False

# 6. 配置 Pipeline
ITEM_PIPELINES = {
   'sinaSpider.pipelines.SaveItems': 300,
}

# 7. 彻底关闭 AutoThrottle (自动限速)，防止系统自动减速
AUTOTHROTTLE_ENABLED = False

# 日志配置
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_LEVEL = 'INFO'