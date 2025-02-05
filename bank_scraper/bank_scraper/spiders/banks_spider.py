
import scrapy
from bank_scraper.items import BankingItem  

class BanksSpider(scrapy.Spider):
    name = "banks_spider"
    allowed_domains = ["https://www.dfcc.lk/", "https://www.sampath.lk/"]  
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
    }

    def parse(self, response):
        # Extract text content
        text = response.xpath('//body//text()').getall()
        cleaned_text = ' '.join([t.strip() for t in text if t.strip()])

        # Create and yield an item
        item = BankingItem()
        item['url'] = response.url
        item['content'] = cleaned_text
        yield item

        # Follow links to other pages (e.g., pagination)
        for next_page in response.css('a.next-page::attr(href)').getall():
            yield response.follow(next_page, self.parse)
