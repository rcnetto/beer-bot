# -*- coding: utf-8 -*-

BOT_NAME = 'products'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'

SPIDER_MODULES = ['homebrew.spiders']
NEWSPIDER_MODULE = 'homebrew.spiders'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True
CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 5.0
