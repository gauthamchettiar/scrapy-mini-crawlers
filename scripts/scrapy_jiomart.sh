# Run jio-by-category crawler
export SCRAPY_PROJECT=jiomart
scrapy crawl jio-by-category

# clean fetched data
python3 jiomart/cleaners/extract_quantity.py