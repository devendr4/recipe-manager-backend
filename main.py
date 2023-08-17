from fastapi import BackgroundTasks, FastAPI, Request
from scrapy.crawler import CrawlerProcess

from ingredients.ingredients.spiders.plansuarez_spider import PlanSuarezSpider

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "hello wrld"}


@app.get("/ingredient")
async def get_ingredient(req: Request, bt: BackgroundTasks):
    print(req.body)
    process = CrawlerProcess(
        {"USER_AGENT": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"}
    )

    process.crawl(PlanSuarezSpider)
    data = process.start()

    # data = bt.add_task(process.start, stop_after_crawl=False)
    print("DATa", data)
    return {"crawled": data}
