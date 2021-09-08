import scrapy
from scrapy.crawler import CrawlerProcess
from ..items import ProjekatPszItem

class CetiriZida(scrapy.Spider):
    name = "4zida"

    def start_requests(self):
        modes = ['prodaja-stanova', 'prodaja-kuca', 'izdavanje-stanova', 'izdavanje-kuca']
        for mode in modes:
            yield scrapy.Request(url="https://www.4zida.rs/" + mode,
                                 callback=self.parse)

    def parse(self, response):
        page_cnt_str = response.xpath('//ul[@class="pagination"]/li[9]/a/text()').extract_first()
        page_cnt = int(page_cnt_str)
        for i in range(1, page_cnt+1):
            yield response.follow(url=response.url + "?strana=" + str(i),
                                  callback=self.parse_page)

    def parse_page(self, response):
        links = response.css('app-search-ad .title-and-subtitle > a').xpath('./@href').extract()
        for link in links:
            yield response.follow(url="https://4zida.rs" + link,
                                  callback=self.parse_ad)

    def parse_ad(self, response):

        item = ProjekatPszItem()
        item['url'] = response.url
        url_parts = response.url.split('/')

        ### sale_rent/apt_house
        item['sale_rent'] = 1 if (url_parts[3] == 'izdavanje') else 0
        item['apt_house'] = 1 if (url_parts[4] == 'kuce') else 0

        loc_crumbs = response.css('.breadcrumb .breadcrumb-item a::text').extract()
        del loc_crumbs[-1]
        del loc_crumbs[0:2]
        ### city
        item['city'] = loc_crumbs[0]
        ### city area
        item['city_area'] = None
        if len(loc_crumbs) > 1:
            item['city_area'] = loc_crumbs[1]
        if len(loc_crumbs) > 2 and (loc_crumbs[1] == 'Gradske lokacije' or loc_crumbs[1] == 'Okolne lokacije'):
            item['city_area'] = loc_crumbs[2]

        ### price
        item['price'] = int(response.xpath('//*[@itemprop="price"]/text()').extract_first().replace('.', ''))

        info = {}
        ### basic-info
        basic_info = response.css('.row.basic-info > div')
        for inf in basic_info:
            prop = inf.xpath('./span[1]/text()').extract_first()
            value = inf.xpath('./span[2]//text()').extract()
            value = ' '.join(value)
            info[prop] = value

        ### additional-info
        add_info = response.css('div.additional-info > div')
        for inf in add_info:
            prop = inf.xpath('./div[1]/text()').extract_first()
            value = inf.xpath('./div[2]//span/text()').extract()
            value = ' '.join(value)
            info[prop] = value

        area = None
        year = None
        yard_area = None
        floor = None
        total_floors = None
        legalized = None
        heating = None
        rooms = None
        bathrooms = None
        if 'Površina' in info:
            area = float(info['Površina'][:-4])
        if 'Godina izgradnje:' in info:
            year = int(info['Godina izgradnje:'])
        if 'Plac oko kuće:' in info:
            yard_area = float(info['Plac oko kuće:'][1:-3])
        if 'Sprat' in info:
            floor = info['Sprat']
            floor = floor.strip()
            floor = floor.replace('sprat', '')
            if floor.find('/') != -1:
                spl = floor.split('/')
                floor = spl[0].strip()
                total_floors = int(spl[1].replace(' ', ''))
        if 'Uknjiženost' in info:
            legalized = 1 if (info['Uknjiženost'] == 'Uknjiženo') else 0
        if 'Grejanje' in info:
            heating = info['Grejanje']
        if 'Broj soba' in info:
            rooms = float(info['Broj soba'])
        if 'Unutrašnje prostorije:' in info:
            unpro = info['Unutrašnje prostorije:']
            search = unpro.find('Kupatil')
            if search != -1:
                comma = unpro.find(',', 0, search)
                if unpro[search:search + 8] == 'Kupatilo':
                    bathrooms = 1
                else:
                    num = unpro[comma + 1:search]
                    num = num.replace(' ', '')
                    bathrooms = int(num)

        item['area'] = area
        item['year'] = year
        item['yard_area'] = yard_area
        item['floor'] = floor
        item['total_floors'] = total_floors
        item['legalized'] = legalized
        item['heating'] = heating
        item['rooms'] = rooms
        item['bathrooms'] = bathrooms
        yield item