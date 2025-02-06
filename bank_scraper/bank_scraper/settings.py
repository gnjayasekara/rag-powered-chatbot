# Scrapy settings for bank_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "bank_scraper"

SPIDER_MODULES = ["bank_scraper.spiders"]
NEWSPIDER_MODULE = "bank_scraper.spiders"


# Selenium Settings
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = None  # WebDriverManager will handle this
SELENIUM_DRIVER_ARGUMENTS = ['--headless', '--disable-blink-features=AutomationControlled']

# Scrapy Settings
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 2
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 5
RETRY_TIMES = 2
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]

# Item Pipelines
ITEM_PIPELINES = {
    'bank_scraper.pipelines.TextChunkingPipeline': 300,
}

# Middleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy_selenium.SeleniumMiddleware': 800,
}
# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
