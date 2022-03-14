from scrapy import Request
from .base_spider import BaseSpider

class TopDealsSpider(BaseSpider):
    name = 'jio-by-url'
    
    def start_requests(self):
        urls = self.settings.get("URLS")
        pincode = self.settings.get("PINCODE")
        for category, url in urls.items(): 
            yield Request(
                url,
                self.parse_items, 
                cookies={'nms_mgo_pincode' : pincode},
                cb_kwargs=dict(category=category)
                )