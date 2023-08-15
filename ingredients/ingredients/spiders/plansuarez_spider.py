from pathlib import Path

import scrapy
from scrapy_splash import SplashRequest


class PlanSuarezSpider(scrapy.Spider):
    name = "plan_suarez"

    def start_requests(self):
        url = "http://localhost:8050/render.html?url=https://www.plansuarez.com/index.php?route=product/search&search=azucar"
        # url = "https://www.plansuarez.com/index.php?route=product/search&search=azucar"
        print("S T A R T I N G")

        yield SplashRequest(
            url=url,
            callback=self.parse,
        )

    # from pathlib import Path
    def parse(self, response):
        print("P A R S I N G")
        products = response.css("body")

        Path("test.html").write_bytes(response.body)
        print("products", products)
        for i in products:
            print({"price": i.css("span.price-normal::text").get()})
            yield {
                "price": i.css("span.price-normal::text").get(),
                "name": i.css("div.name").css("a::text").get(),
            }


# from pathlib import Path
#
# import scrapy
#
#
# class FarmatodoSpider(scrapy.Spider):
#     name = "farmatodo"
#
#     def start_requests(self):
#         urls = [
#             "https://quotes.toscrape.com/page/1/",
#             "https://quotes.toscrape.com/page/2/",
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f"quotes-{page}.html"
#         print(filename)
#         # Path(filename).write_bytes(response.body)
#         self.log(f"Saved file {filename}")
