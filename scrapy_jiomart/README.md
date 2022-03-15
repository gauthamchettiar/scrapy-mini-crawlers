# SCRAPY MINI CRAWLERS : scrapy_jiomart

## Disclaimer
1. Cannot guarantee it's working, as website may change it's structure or URL at any point in time and I might not keep it up-to-date with those changes.
2. Use Responsibly!

## Features
1. Scrap product pages of https://jiomart.com for inventory Items.
2. Fetches Name, Price and Category of a particular Item.
    ```json
    { 
        "name": "Tomato 1 kg", 
        "price": 35.0, 
        "category": "Fruits & Vegetables"
    }
    ```
3. Has [Feeds](https://docs.scrapy.org/en/latest/topics/feed-exports.html#std-setting-FEEDS) to export data to json or s3, bucketed nicely as per month - 
    ```
    ├── scraped_data
    └── jiomart
        └── 202203
            └── 20220315.json
    ```
4. Can scrap a particular category item listed under https://www.jiomart.com/all-category.
5. Can scrap any custom product listing URL, e.g: https://www.jiomart.com/c/groceries/bestdeals/hot-food-fest-2022/4515.
6. Can change `PINCODE` in setting to fetch items for a particular area.


## Spiders
1. jio-by-category : 
    ```python
    # related settting @ settings.py
    URL_CATEGORY = "https://www.jiomart.com/all-category"
    CATEGORIES_TO_PARSE = ["Fruits & Vegetables"]
    ```
2. jio-by-top-deals : 
    ```python
    # related settting @ settings.py
    URL_TOP_DEALS = "https://www.jiomart.com/all-topdeals"
    ```
3. jio-by-url : 
    ```python
    # related settting @ settings.py
    URLS = {
    "Hotspot Deals" : "https://www.jiomart.com/c/groceries/bestdeals/hotspot/706",
    "Hot Food Fest" : "https://www.jiomart.com/c/groceries/bestdeals/hot-food-fest-2022/4515"
    }
    ```

## Usage
```bash
# set default.setting @ scrapy.cfg as
#   [settings]
#   default = scrapy_jiomart.settings

# run a spider
scrapy crawl jio-by-category
```
