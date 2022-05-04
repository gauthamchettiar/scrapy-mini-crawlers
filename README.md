# SCRAPY MINI CRAWLERS
Just a repository of useful crawlers implemented using [scrapy](https://github.com/scrapy/scrapy) to collect somewhat useful data.

README has been provided for individual crawlers, refer links below for additional information.

Currently includes following scrapers,
1. [jiomart](jiomart/) : Crawls https://jiomart.com for inventory items.


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
    # Set project simply by setting an env variable,
    
    # export SCRAPY_PROJECT=<project-name>
    export SCRAPY_PROJECT=jiomart

    # Refer 'scrapy.cfg' file for complete list of projects available
    ```
5. Run a spider (crawler) :
    ```bash
    # scrapy crawl <crawler-name> <optional-params>
    scrapy crawl jio-by-top-deals

    # Run below command to get all spiders(crawlers) defined for a project
    scrapy list
    ```
6. Crawled data will be available at `scraped_data/` folder.