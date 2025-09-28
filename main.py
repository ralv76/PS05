import scrapy
from scrapy.crawler import CrawlerProcess

class DivanSpider(scrapy.Spider):
    name = "divan"
    allowed_domains = ["divan.ru"]
    start_urls = [
        "https://www.divan.ru/category/svet?sort=0",
        "https://www.divan.ru/category/svet/page-2?sort=0", 
        "https://www.divan.ru/category/svet/page-3?sort=0",
        "https://www.divan.ru/category/svet/page-4?sort=0",
        "https://www.divan.ru/category/svet/page-5?sort=0"
    ]

    def parse(self, response):
        lights = response.css('div._Ud0k')
        for light in lights:
            yield {
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('div.pY3d2 span::text').get(),
                'url': 'https://www.divan.ru' + light.css('a').attrib['href']
            }

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'result.txt'
    })
    process.crawl(DivanSpider)
    process.start()