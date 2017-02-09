import scrapy
from scholar.items import ScholarItem


class CiteSpider(scrapy.Spider):
    name = "citation"
    page_size = 20
    start = 0
    # urls = 'https://scholar.google.com/citations?user=nbPXtEUAAAAJ&hl=en'
    urls = 'https://scholar.google.com/citations?user=EXATcMAAAAAJ&hl=en'
    start_urls = [urls + '&cstart={}&pagesize={}'.format(start, page_size)]

    def parse(self, response):
        if response.css("td.gsc_a_t").extract_first() is not None:
            for paper in response.css("td.gsc_a_t"):
                paper_title = paper.css("a::text").extract_first()
                paper_authors = paper.css("div.gs_gray::text").extract_first()

                item = ScholarItem()
                item['title'] = paper_title
                item['authors'] = paper_authors
                yield item

            CiteSpider.start += CiteSpider.page_size
            next_page = CiteSpider.start_urls[0] + '&cstart={}&pagesize={}'.format(CiteSpider.start, CiteSpider.page_size)
            yield scrapy.Request(next_page, callback=self.parse)

            for cite in response.css('td.gsc_a_c a::attr(href)').extract():
                if len(cite) > 0:
                    yield scrapy.Request(cite, callback=self.parse2)

    def parse2(self, response):

        for paper in response.css('div.gs_ri'):

            item = ScholarItem()
            item['title'] = paper.css('h3.gs_rt a::text').extract_first()
            item['authors'] = paper.css('div.gs_a::text').extract_first()
            yield item

            next_page = response.xpath('//span[@class="gs_ico gs_ico_nav_next"]/../@href').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse2)
