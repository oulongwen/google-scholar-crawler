# Google Scholar crawler

This is a Google Scholar scrawler that downloads all the publications of an author and all the publications that cited this author.

## Prerequisites
This program works for `Python3` and requires the `Scrapy` package. You can install `Scrapy` by running the folowing command in your terminal:
```bash
pip3 install Scrapy
```

## Usage
In order to run the code, specify the url of the profile of the author to crawl in the *cite_spider.py* file in the *spiders* folder. For instance:

```
urls = 'https://scholar.google.com/citations?user=EXATcMAAAAAJ&hl=en'
```

Then start the crawler by running:

```
scrapy crawl citation -o citation.jl
```

The `-o` option specifies the output file that stores the extracted data. `Scrapy` supports four formates: JSON, JSON lines, CSV and XML.

## Issues
If there are too many pages to crawl, i.e., the author has too many publications and too many citations, the program may not be able to finish the crawlilng process since it may be interrupted by the host.
