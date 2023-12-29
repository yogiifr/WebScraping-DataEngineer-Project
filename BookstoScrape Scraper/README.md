# Bookstoscrape Books Scraper

## Project Description
The Bookstoscrape Books Scraper is a Python web crawler built with the Scrapy framework to extract information about books from books.toscrape.com The crawler follows specific rules to navigate through the website and scrape details such as book title, price (£), and availability.

## Steps
1. **Importing Required Modules:** 
```python
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
```
The script starts by importing necessary modules from the Scrapy framework. `CrawlSpider` is a specialized spider class in Scrapy for crawling websites, and `Rule` is used to define rules for crawling and parsing. `LinkExtractor` helps in extracting links from web pages.

2. **Spider Class Definition:** 
```python
class CrawlerSpider(CrawlSpider):
    name = "bookcrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
```
A new spider class named `CrawlerSpider` is defined, inheriting from `CrawlSpider`. The spider is named "bookcrawler" and is configured to crawl the domain "toscrape.com" starting from the specified URL.

3. **Rules for Crawling:** 
```python
    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item"),
    )
```
Two rules are defined using the `Rule` class. The first rule is for following links that match the pattern "catalogue/category". The second rule is for following links that match "catalogue" but do not contain "category" (this is achieved using the `deny` parameter). For each matched link, the `parse_item` method will be called.

4. **Parsing Method:** 
```python
    def parse_item(self, response):
        yield {
            "title"         : response.css(".product_main h1::text").get(),
            "price_£"         : response.css(".price_color::text").get().replace("£",""),
            "availability"  : response.css(".availability::text")[1].get().replace("\n", "").replace("    ", "").replace("In stock ", "").replace("(", "").replace("available)", ""),
        }

```
The `parse_item` method is responsible for extracting information from the web pages that match the second rule. It uses CSS selectors to extract the book title, price (in pounds), and availability. The extracted data is then yielded as a dictionary.


## Video Reference
For a visual guide and additional insights, you can refer to the following video:

**Title:** Coding Web Crawler in Python with Scrapy

**Link:** [Watch PLaylist](https://www.youtube.com/watch?v=m_3gjHGxIJc)
