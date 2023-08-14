import scrapy


class IngredientspiderSpider(scrapy.Spider):
    name = "ingredientspider"
    allowed_domains = ["farmatodo.com.ve"]
    start_urls = ["https://farmatodo.com.ve"]

    def parse(self, response):
        pass
