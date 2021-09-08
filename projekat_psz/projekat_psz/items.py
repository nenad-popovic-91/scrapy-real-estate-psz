# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ProjekatPszItem(Item):
    sale_rent = Field() # bool
    apt_house = Field() # bool
    city = Field() # str
    city_area = Field() # str
    price = Field() # int
    area = Field() # float
    year = Field() # int
    yard_area = Field() # float
    floor = Field() # str
    total_floors = Field() # int
    legalized = Field() # bool
    heating = Field() # str
    rooms = Field() # float
    bathrooms = Field() # int
    url = Field() # str

