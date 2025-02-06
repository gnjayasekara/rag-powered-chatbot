
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class BanksSpider(scrapy.Spider):
    name = "banks_spider"
    
    allowed_domains = ["dfcc.lk", "sampath.lk"]  
    start_urls = [
        "https://www.dfcc.lk/interest-rates/",
        "https://www.dfcc.lk/interest-rates/fd-rates/",
        "https://www.dfcc.lk/interest-rates/lending-rates/",
        "https://www.dfcc.lk/interest-rates/senior-citizen-fd-rate/",
        "https://www.dfcc.lk/dfcc-cards/credit-cards/card-comparison/",
        "https://www.dfcc.lk/contact-us/",
        "https://www.dfcc.lk/faq/",
        "https://www.dfcc.lk/leasing-faqs/",
        "https://www.dfcc.lk/online-banking-faqs/",
        "https://www.sampath.lk/personal-banking/term-deposit-accounts/regular-deposits/Fixed-Deposits?category=personal_banking",
        "https://www.sampath.lk/personal-banking/loan/housing-loans/Sevana-Housing-Loan?category=personal_banking",
        "https://www.sampath.lk/sampath-cards?firstTab=6&secondTab=4&thirdTab=1",
        "https://www.sampath.lk/sampath-cards?firstTab=6&secondTab=5",
        "https://www.sampath.lk/digital-banking?type_name=online-banking&section_name=Sampath-Corporate-Payment-System",
        "https://www.sampath.lk/contact-us"
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # Respectful delay between requests (2 seconds)
        'USER_AGENT': 'Mozilla/5.0 (compatible; YourBot/1.0; +http://yourwebsite.com)',
        'ROBOTSTXT_OBEY': True,  # Respect robots.txt rules
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 1,
        'AUTOTHROTTLE_MAX_DELAY': 5,
        'SELENIUM_DRIVER_NAME': 'chrome',
        'SELENIUM_DRIVER_EXECUTABLE_PATH': 'C:/chromedriver-win64/chromedriver.exe', # Path to the chromedriver executable
        'SELENIUM_DRIVER_ARGUMENTS': ['--headless', '--disable-blink-features=AutomationControlled'], 
    }

    def __init__(self, *args, **kwargs):
        super(BanksSpider, self).__init__(*args, **kwargs)
        # Define the path to the ChromeDriver and create the service
        self.driver_service = Service('C:/chromedriver-win64/chromedriver.exe') 
        self.driver_service.start()

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        driver = response.request.meta['driver']

        try:
            # Wait for dynamic content to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except TimeoutException:
            self.logger.error("Timeout waiting for page to load")
            return
        
        # Get fully rendered HTML
        page_source = driver.page_source
        response = scrapy.Selector(text=page_source)

        # Extract text content
        text = response.xpath('//body//text()').getall()
        cleaned_text = ' '.join([t.strip() for t in text if t.strip()])

        yield {
            "url": response.url,
            "content": cleaned_text
        }


        # Follow links to other pages (e.g., pagination)
        for next_page in response.css('a.next-page::attr(href)').getall():
            yield response.follow(next_page, self.parse)
