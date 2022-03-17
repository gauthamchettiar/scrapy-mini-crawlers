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
    ├── scraped_data                    <- all scraped data are placed here
    └── jiomart                         <- project specific folder
        └── 202203                      <- Year + Month (bucket)
            └── 20220315_110001.json    <- Year+Month+Day _ Pincode (file_name)
    ```
4. Can scrap a particular category item listed under https://www.jiomart.com/all-category.
5. Can scrap any custom product listing URL, e.g: https://www.jiomart.com/c/groceries/bestdeals/hot-food-fest-2022/4515.
6. Can change `PINCODE` @ setting to fetch items for a particular area.
7. Can clean the fetched data,
    a. Extract 'quantity' from name of any item
    b. Places cleaned data @ `cleaned_data/jiomart`, follows same bucketing schema like `scraped_data`
    b. Places error data (if any) @ `error_data/jiomart`, follows same bucketing schema like `scraped_data` - [more](#cleaning-fetched-data)

## Spiders
1. jio-by-category : 
    ```python
    # related settting @ scrapy_jiomart/settings.py
    URL_CATEGORY = "https://www.jiomart.com/all-category"
    CATEGORIES_TO_PARSE = ["Fruits & Vegetables"]
    ```
2. jio-by-top-deals : 
    ```python
    # related settting @ scrapy_jiomart/settings.py
    URL_TOP_DEALS = "https://www.jiomart.com/all-topdeals"
    ```
3. jio-by-url : 
    ```python
    # related settting @ scrapy_jiomart/settings.py
    URLS = {
    "Hotspot Deals" : "https://www.jiomart.com/c/groceries/bestdeals/hotspot/706",
    "Hot Food Fest" : "https://www.jiomart.com/c/groceries/bestdeals/hot-food-fest-2022/4515"
    }
    ```

## Usage
### Fetching Data
```bash
# Set Project
export SCRAPY_PROJECT=scrapy_jiomart

# Get a list of defines spiders
scrapy list
# > jio-by-category
# > jio-by-top-deals
# > jio-by-ur

# Run a spider
scrapy crawl jio-by-category
```
### Cleaning Fetched Data
Cleaner have been provided @ `scrapy_jiomart/cleaners/extract_quantity.py`.

Run below command to invoke cleaning job,
```bash
python scrapy_jiomart/cleaners/extract_quantity.py
```
Above command will do following things,
1. Checks for any uncleaned file from 'scraped_data/jiomart'. 
2. Uses rules defined in 'cleaning_rules.json' to - 
  a. filter out unwanted items and 
  b. extract quantity and type from name
3. Stores cleaned files at 'cleaned_data/jiomart'.
4. Stores Error Data at 'error_data/jiomart', this data includes items
  a. items for which there is no rules present (<file_name>-new_entry.json)
  b. items for which riles were present but regex did not match (<file_name>-no_regex_rule.json)