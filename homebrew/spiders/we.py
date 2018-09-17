# -*- coding: utf-8 -*-
import scrapy


class WeSpider(scrapy.Spider):
    name = "weconsultoria.com.br"
    allowed_domains = ["weconsultoria.com.br"]
    start_urls = [
        'https://loja.weconsultoria.com.br/ingredientes-s10012/',
        'https://loja.weconsultoria.com.br/equipamentos-s10011/',
        'https://loja.weconsultoria.com.br/embarrilamento-s10010/',
        'https://loja.weconsultoria.com.br/cervejarias-s10008/',
        'https://loja.weconsultoria.com.br/kits-s10013/',
        'https://loja.weconsultoria.com.br/outros-s10015/'
    ]
    headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
    }

    def make_requests_from_url(self, url):
            return scrapy.http.Request(url, headers=self.headers)

    def parse(self, response):
        for page_url in response.css("ul.products > li > div.product > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(page_url), callback=self.parse_item_page)
        next_page = response.css("span.page-next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_item_page(self, response):
        item = {}
        product = response.css("div#interactivity")
        item["id"] = product.css("h1.product-title ::text").extract_first()
        item["nome"] = product.css("dt.item > span ::text").extract_first()
        item['categoria'] = product.css("span.posted_in > a ::text").extract()
        item['preco'] = product.css("div.price-wrapper ::text").extract()[3]
        yield item
