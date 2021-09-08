import scrapy
from scrapy.crawler import CrawlerProcess
from ..items import ProjekatPszItem

class Nekretnine(scrapy.Spider):
    name = "nekretnine"

    def start_requests(self):
        modes = ['/stanovi/izdavanje-prodaja/prodaja/', '/kuce/izdavanje-prodaja/prodaja/', '/stanovi/izdavanje-prodaja/izdavanje/', '/kuce/izdavanje-prodaja/izdavanje/']
        for mode in modes:
            yield scrapy.Request(url="http://www.nekretnine.rs/stambeni-objekti" + mode + 'lista/po-stranici/10/',
                                 callback=self.parse)

    def parse(self, response):
        page_cnt_str = response.xpath('//span[contains(text(), "pronadjenih oglasa")]/text()').extract_first()
        page_cnt = (int(page_cnt_str[:-19]) + 19) // 20
        if page_cnt > 500:
            page_cnt = 500
        for i in range(1, page_cnt+1):
             yield response.follow(url=response.url + "stranica/" + str(i) + "/",
                                   callback=self.parse_page)

    def parse_page(self, response):
        links = response.css('.row.offer h2 > a').xpath('./@href').extract()
        for link in links:
            yield response.follow(url="http://www.nekretnine.rs" + link,
                                  callback=self.parse_ad)

    def parse_ad(self, response):
        item = ProjekatPszItem()
        item['url'] = response.url

        url_parts = response.url.split('/')

        # apt_house
        item['apt_house'] = 1 if (url_parts[4] == 'kuce') else 0
        item['sale_rent'] = 0 if (response.css('.detail-seo-subtitle::text').extract_first().find('Prodaja') != -1) else 1

        # location
        loc_strings = response.css('.stickyBox__Location::text').extract_first()
        if loc_strings.find(', ') != -1:
            loc_strings = loc_strings.split(', ')
            item['city'] = loc_strings[0]
            item['city_area'] = loc_strings[1]
        else:
            item['city'] = loc_strings
            item['city_area'] = None

        # price
        item['price'] = int(response.css('.stickyBox__price::text').extract_first().replace(' ', '').replace('EUR', ''))
        # area
        item['area'] = float(response.css('.stickyBox__size::text').extract_first()[:-2])

        ### main details
        main_details = response.css('.property__main-details > ul')

        rooms = main_details.xpath('./li[2]/span/text()').extract_first()
        item['rooms'] = float(rooms) if (rooms != '-') else None

        bathrooms = main_details.xpath('./li[3]/span/text()').extract_first()
        item['bathrooms'] = float(bathrooms) if (bathrooms != '-') else None

        item['heating'] = main_details.xpath('./li[4]/span/text()').extract_first()

        # amenities
        info = {}
        amenities = response.xpath('//section[@id="sadrzaji"]/div[1]/ul/li/text()').extract()
        for i in range(0, len(amenities)):
            amenities[i] = amenities[i].strip().split(':\n ')
            info[amenities[i][0]] = amenities[i][1].lstrip()

        item['floor'] = info['Sprat'] if ('Sprat' in info) else None
        item['total_floors'] = int(info['Ukupan brој spratova']) if ('Ukupan brој spratova' in info) else None
        item['legalized'] = 1 if ('Uknjiženo' in info and info['Uknjiženo'] == 'Da') else 0
        item['year'] = int(info['Godina izgradnje']) if ('Godina izgradnje' in info) else None
        item['yard_area'] = float(info['Površina zemljišta'][:-3]) if ('Površina zemljišta' in info) else None

        yield item