# SCRAPY MINI CRAWLERS
Just a repository of useful crawlers implemented using [scrapy](https://github.com/scrapy/scrapy) to collect somewhat useful data.

README has been provided for individual crawlers, refer links below for additional information.

Currently includes following scrapers,
1. [scrapy_jiomart](scrapy_jiomart/) : Crawls https://jiomart.com for inventory items.


## Disclaimer
1. Cannot guarantee it's working, as website may change it's structure or URL at any point in time and I might not keep it up-to-date with those changes.
2. Use Responsibly!


## Usage (directly from repo)
1. Clone the Repository : 
    ```bash
    git clone https://github.com/gauthamchettiar/scrapy-mini-crawlers.git
    ```
2. Create virtual env : 
    ```bash
    python -m venv .env

    # linux/macOS
    source .env/bin/activate
    ```
3. Install python dependencies : 
    ```bash
    pip install -r requirements.txt
    ```
4. Set project : 
    ```bash
    # Refer individual project, for projects settings string
    # change 'settings.default' in 'scrapy.cfg'
    [settings]
    default = scrapy_jiomart.settings
    ```
5. Run crawler :
    ```bash
    # scrapy crawl <crawler-name> <optional-params>
    scrapy crawl jio-by-top-deals
    ```
6. Crawled data will be available at 'scraped_data/' folder.