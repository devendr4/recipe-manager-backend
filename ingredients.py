import scrapy


class IngredientsSpider(scrapy.Spider):
    name = "ingredients"
    allowed_domains = ["farmatodo.com.ve"]
    start_urls = ["https://www.farmatodo.com.ve/buscar?product=azucar"]

    def parse(self, response):
        pass
