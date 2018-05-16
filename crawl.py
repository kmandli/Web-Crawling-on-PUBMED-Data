import scrapy
from items import LinkItem
from scrapy.crawler import CrawlerProcess


class WikiLinks(scrapy.Spider):

    count = 0
    name = 'wiki_scrap'
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Web_Bot"]

    def parse(self, response):
        string = '/wiki/Web_Bot'
        base_url = "https://en.wikipedia.org"
        end = '/wiki/Automated_bot'
        linkList = []
        for sel in response.xpath("//*[contains(@id, 'bodyContent')]//a"):
            url = sel.xpath('@href').extract_first()
            name = sel.xpath('text()').extract_first()  
            if url and name:
                count = 0
                if url.startswith('/wiki/'):
                    link = LinkItem()
                    link['url'] = url.encode('utf-8').strip()
                    link['name']  = name.encode('utf-8').strip()
                    if '#' in link['url']:
                        continue
                    elif link['url'] == string:
                        print link['url']
                    else:
                        linkList.append(link)
        return linkList
                        #return link
                        #yield response.follow(base_url + link['url'],self.parse2)

    def parse2(self,response):
        end = '/wiki/Automated_bot'
        count += 1
        for sel in response.xpath("//*[contains(@id, 'bodyContent')]//a"):
            url = sel.xpath('@href').extract_first()
            name = sel.xpath('text()').extract_first()  
            if url and name:
                if url.startswith('/wiki/'):
                    link = LinkItem()
                    link['url'] = url.encode('utf-8').strip()
                    link['name']  = name.encode('utf-8').strip()
                    if '#' in link['url']:
                        continue
                    elif link['url'] == end:
                        print link['url']
                    else:
                        yield link
 
process = CrawlerProcess()

process.crawl(WikiLinks)
process.start()
