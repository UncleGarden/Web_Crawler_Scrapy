from scrapy.item import Item, Field

class MiAppStoreItem(Item):
    title = Field()
    link = Field()