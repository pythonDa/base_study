# -*- coding: utf-8 -*-

# Scrapy settings for splash_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from fake_useragent import UserAgent
BOT_NAME = 'splash_test'
SPIDER_MODULES = [
 'splash_test.spiders']
NEWSPIDER_MODULE = 'splash_demo.spiders'
USER_AGENT = UserAgent().chrome
ROBOTSTXT_OBEY = False
SPLASH_URL = 'http://192.168.99.100:8050'
DOWNLOADER_MIDDLEWARES = {'splash_demo.middlewares.SplashTestDownloaderMiddleware':543,
 'scrapy_splash.SplashCookiesMiddleware':723,
 'scrapy_splash.SplashMiddleware':725,
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware':810}
SPIDER_MIDDLEMARES = {'scrapy_splash.SplashDeduplicateArgsMiddleware': 100}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
# okay decompiling settings.cpython-38.pyc
