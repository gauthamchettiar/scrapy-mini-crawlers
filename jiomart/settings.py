from datetime import datetime
from os.path import abspath, curdir
# Scrapy settings for jiomart project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jiomart'

SPIDER_MODULES = ['jiomart.spiders']
NEWSPIDER_MODULE = 'jiomart.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jiomart (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
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
#    'jiomart.middlewares.ScrapyJiomartSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jiomart.middlewares.ScrapyJiomartDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jiomart.pipelines.ScrapyJiomartPipeline': 300,
#}

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

# Custom Headers Required for Functioning of given Spider
# Since each area has different products listed, PINCODE governs which area to parse data from
PINCODE = "400706"

# URL for top-deals
URL_TOP_DEALS = "https://www.jiomart.com/all-topdeals"
# For any custom URL that is short-lived, e.g: promotions
#   Make sure each URL is a direct link to item listing
URLS = {
    "Hotspot Deals" : "https://www.jiomart.com/c/groceries/bestdeals/hotspot/706",
    "Hot Food Fest" : "https://www.jiomart.com/c/groceries/bestdeals/hot-food-fest-2022/4515"
}

# In case you need to parse a particular category, you can mention the categories below
URL_CATEGORY = "https://www.jiomart.com/all-category"
CATEGORIES_TO_PARSE = ["Fruits & Vegetables"]


# Configure AWS Parameters to upload files
# AWS_BUCKET_NAME = ""
#AWS_ACCESS_KEY_ID = ""
#AWS_SECRET_ACCESS_KEY = ""

# Function to get partitioned monthly by folder and file
def get_partitioned_path(timestamp:datetime):
    return f"{timestamp.strftime('%Y%m')}/{timestamp.strftime('%Y%m%d')}"

# Feeds - places where you need to upload/keep the scraped files
# TIP: You can comment it out and use --output instead
FEEDS = {
        f"file:///{abspath(curdir)}/scraped_data/jiomart/{get_partitioned_path(datetime.now())}_{PINCODE}.json": {
            'format': 'json',
            'overwrite': True
        },
        f"s3://{AWS_BUCKET_NAME}/scraped_data/jiomart/{get_partitioned_path(datetime.now())}_{PINCODE}.json": {
           'format': 'json',
           'overwrite': True
        }
    }