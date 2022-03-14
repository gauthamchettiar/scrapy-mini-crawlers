from scrapy import Request
from .base_spider import BaseSpider

class TopDealsSpider(BaseSpider):
    name = 'jio-by-top-deals'
    
    def start_requests(self):
        url = self.settings.get("URL_TOP_DEALS")
        pincode = self.settings.get("PINCODE")

        yield Request(
            url,
            self.parse_items, 
            cookies={'nms_mgo_pincode' : pincode},
            cb_kwargs=dict(category="Top Deals")
            )