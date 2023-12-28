import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ProductsSpider(CrawlSpider):
    name = "products"
    allowed_domains = ["yamaha-motor.co.id"]
    start_urls = ["https://www.yamaha-motor.co.id/products/"]

    rules = (
        Rule(LinkExtractor(allow=(r"category",))),
        Rule(LinkExtractor(allow=(r"product",)), callback='parse_item'), 
    )

    def parse_item(self, response):
        pass
