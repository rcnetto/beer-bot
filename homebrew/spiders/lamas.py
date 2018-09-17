# -*- coding: utf-8 -*-
import scrapy
import logging


class LamasSpider(scrapy.Spider):
    name = "lamasbrewshop.com.br"
    allowed_domains = ["loja.lamasbrewshop.com.br"]
    initial_url = 'http://loja.lamasbrewshop.com.br'
    headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
    }

    def make_requests_from_url(self, url):
        return scrapy.http.Request(url, headers=self.headers)

    def start_requests(self):
        logging.info("Initial URL: %s", self.initial_url)
        yield scrapy.Request(url=self.initial_url, callback=self.process_initial)
    
    def process_initial(self, response):
        for category_url in response.css("li.level0 > a ::attr(href)").extract():
            logging.info("Category URL: %s", category_url)
            yield scrapy.Request(response.urljoin(category_url), callback=self.parse)

    def parse(self, response):
        for page_url in response.css("li.item > a ::attr(href)").extract():
            logging.info("Parsing URL: %s", page_url)
            yield scrapy.Request(response.urljoin(page_url), callback=self.parse_item_specific_page)
        next_page = response.css("li > a.next ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_item_page(self, response):
        for product in response.css("li.item"):
            item = {}
            item["id"] = product.css("a ::attr(href)").extract_first()
            item["nome"] = product.css("a ::attr(title)").extract_first()
            item['categoria'] = product.css("div.NomeCategoria > a ::text").extract_first().replace('\n', '').replace('\t', '')
            item['preco'] = response.css('span.price ::text').extract_first().replace('R$', '')
            item['url'] = product.css("a ::attr(href)").extract_first()
            yield item

    def parse_item_specific_page(self, response):
        item = {}
        product = response.css("div.product-info")
        item["id"] = product.css("p.name.product-title > a ::attr(href) ").extract_first()
        item["nome"] = product.css("h1.product-title ::text").extract_first()
        #item['categoria'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").extract_first()
        #item['categoria'] = product.css("p.category ::text").extract_first().replace('\n', '').replace('\t', '')
        item['categoria'] = product.css("span.posted_in > a ::text").extract()
        #item['descricao'] = product.css("div.product-short-description ::text").extract()
        item['preco'] = product.css("div.price-wrapper ::text").extract()[3]
        yield item
