import scrapy


class ZingSpider(scrapy.Spider):
    name = "bim"
    allowed_domains = ['zingnews.vn']
    start_urls = ['https://zingnews.vn', ]
    crawled = 0

    def parse(self, response):
        if response.css('meta[property = "og:type"]::attr("content")').get() == "article":
            self.crawled += 1
            f = open(
                'C:/Users/acer/PycharmProjects/crawl zingnews/crawlzingnews/crawlzingnews/spiders/Output/title.txt',
                'a+', encoding="utf-8")
            f.write('CRAWLED: '+ str(self.crawled)+'\n')
            title = response.css('header.the-article-header h1.the-article-title::text').get()

            f.write('TIÊU ĐỀ: ' + title + '\n')
            summary = response.css('section.main > p.the-article-summary::text').get()
            f.write('TÓM TẮT: ' + summary + '\n')
            f.write('TAGs: ')
            for i in response.css('meta[property = "article:tag"]::attr("content")'):
                tag = i.get()
                f.write(tag + ', ')
            f.write('\n')
            author = response.css('div.the-article-credit p.author::text').get()
            f.write('TÁC GIẢ: ' + author + '\n')
            f.write('NỘI DUNG:' + '\n')
            for i in response.css('div.the-article-body p::text'):
                p_body = i.get()
                f.write(p_body + '\n')
        for link in response.css('p.article-title a::attr(href)').getall():
            yield scrapy.Request(response.urljoin(link), callback=self.parse)

