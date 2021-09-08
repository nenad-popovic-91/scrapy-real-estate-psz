# Scrapy settings for projekat_psz project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'projekat_psz'

SPIDER_MODULES = ['projekat_psz.spiders']
NEWSPIDER_MODULE = 'projekat_psz.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'projekat_psz (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'projekat_psz.middlewares.ProjekatPszSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'projekat_psz.middlewares.ProjekatPszDownloaderMiddleware': 543,
#}


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    # 'rentier_rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    # 'rentier_rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

# ROTATING_PROXY_LIST = [
#     '138.197.2.106:20051',
#     '188.120.245.247:12432',
#     '146.120.95.1:8000',
#     '108.163.66.164:8080',
#     '51.75.162.18:9999',
#     '124.65.117.38:7302',
#     '104.248.63.18:30588',
#     '117.102.84.142:443',
#     '123.136.8.122:3128',
#     '117.102.84.142:443',
#     '49.12.4.194:12110',
#     '152.26.66.140:3128',
#     '69.197.181.202:3128',
#     '13.124.177.38:1080',
#     '54.168.243.133:1080',
#     '54.168.243.133:1080',
#     '190.187.253.124:3128',
#     '187.95.125.71:3128',
#     '201.249.190.235:3128',
#     '49.12.0.103:18445',
#     '175.43.176.182:7302',
#     '209.165.163.187:3128',
#     '49.12.0.103:18445',
#     '213.137.240.243:81',
#     '137.220.33.2:1080',
#     '107.170.42.147:54818',
#     '54.95.178.27:1080',
#     '81.201.60.130:80',
# ]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'projekat_psz.pipelines.ProjekatPszPipeline': 300,
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
