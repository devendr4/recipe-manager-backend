from pathlib import Path

import scrapy
from scrapy_splash import SplashRequest

# lua script
script2 = """
function main(splash, args) assert(splash:go(args.url))
  return {
    html = splash:html(),
  }
end
"""
script = """
function main(splash, args)

    current_scroll = 0

    scroll_to = splash:jsfunc("window.scrollTo")
    get_body_height = splash:jsfunc(
        "function() {return document.body.scrollHeight;}"
    )
    assert(splash:go(splash.args.url))
    splash:wait(3)

    height = get_body_height()

    while current_scroll < height do
        scroll_to(0, get_body_height())
        splash:wait(5)
            current_scroll = height
            height = get_body_height()
    end
    splash:set_viewport_full()
    return splash:html()
end
"""


class PlanSuarezSpider(scrapy.Spider):
    name = "plan_suarez"

    def start_requests(self):
        # url = "https://www.plansuarez.com/index.php?route=product/search&search=azucar"
        url = "https://www.plansuarez.com/index.php?route=product/category&path=252"
        # url = "https://beerwulf.com/en-gb/c/mixedbeercases"
        print("S T A R T I N G")

        yield SplashRequest(
            url=url,
            callback=self.parse,
            endpoint="execute",
            args={"lua_source": script},
        )

    # from pathlib import Path
    def parse(self, response):
        print("P A R S I N G")
        products = response.css("body")

        Path("test.html").write_bytes(response.body)
        print("products", products)
        for i in products:
            print({"price": i.css("span.price-normal::text").get()})
            print(i.css("div.ias-trigger-next"))
            yield {
                "price": i.css("span.price-normal::text").get(),
                "name": i.css("div.name").css("a::text").get(),
            }
