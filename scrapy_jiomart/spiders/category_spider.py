from scrapy import Request
from .base_spider import BaseSpider

class CategorySpider(BaseSpider):
    name = 'jio-by-category'
    
    def start_requests(self):
        url = self.settings.get("URL_CATEGORY")
        pincode = self.settings.get("PINCODE")

        yield Request(
            url, 
            self.parse_categories, 
            cookies={'nms_mgo_pincode' : pincode}
            )

    def parse_categories(self, response):
        categories_to_parse = self.settings.get("CATEGORIES_TO_PARSE")

        for category_detail in response.css("div.cat_details"):
            category_url = category_detail.css("a:first-child::attr(href)").get()
            category_name = category_detail.css("a > span::text").get()
            if category_name in categories_to_parse:
                yield Request(
                    category_url, 
                    self.parse_items, 
                    cookies=response.request.cookies,
                    cb_kwargs=dict(category=category_name)
                    )
