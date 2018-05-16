import scrapy

class LinkItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
