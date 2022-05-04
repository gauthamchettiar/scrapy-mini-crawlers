from scrapy import Spider
from jiomart.items import JiomartInventoryItem

class BaseSpider(Spider):
    def parse_items(self, response, category=None):
        for item_detail in response.css("div.cat-item"):
            yield JiomartInventoryItem(
                name=item_detail.css("span.clsgetname::text").get(),
                price=float(item_detail.css("span#final_price::text").get()[2:].replace(",","")),
                category=category
            )
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_items, cookies=response.request.cookies, cb_kwargs=dict(category=category))
