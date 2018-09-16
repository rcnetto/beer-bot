# -*- coding: utf-8 -*-
import scrapy


class BahiaMalteSpider(scrapy.Spider):
    name = "bahiamalte.com.br"
    allowed_domains = ["www.bahiamalte.com.br"]
    start_urls = [
        'http://www.bahiamalte.com.br/loja',
    ]

    def parse(self, response):
        for page_url in response.css("div.products > div.product-small > div > div.product-small > div.box-image > div > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(page_url), callback=self.parse_item_specific_page)
        next_page = response.css("li > a.next ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_item_page(self, response):
        item = {}
        product = response.css("div.product-small.box")
        item["id"] = product.css("p.name.product-title > a ::attr(href) ").extract_first()
        item["nome"] = product.css("p.name.product-title ::text").extract_first()
        #item['categoria'] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").extract_first()
        item['categoria'] = product.css("p.category ::text").extract_first().replace('\n', '').replace('\t', '')
        #item['descricao'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").extract_first()
        item['preco'] = response.css('span.price ::text').extract()[1]
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
