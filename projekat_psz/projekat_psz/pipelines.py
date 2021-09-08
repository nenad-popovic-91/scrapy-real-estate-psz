# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector


class ProjekatPszPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='passwordPSZ808',
            database='realestate'
        )
        self.cursor = self.conn.cursor()
        # self.create_table()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS ads""")
        self.cursor.execute(
            """CREATE TABLE ads(
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                sale_rent TINYINT NOT NULL,
                apt_house TINYINT NOT NULL,
                city VARCHAR(128),
                city_area VARCHAR(128),
                price FLOAT,
                area FLOAT,
                year INT,
                yard_area FLOAT,
                floor VARCHAR(128),
                total_floors INT,
                legalized TINYINT,
                heating VARCHAR(256),
                rooms FLOAT,
                bathrooms TINYINT,
                url VARCHAR(512)
            )""")

    def process_item(self, item, spider):
        self.cursor.execute("""INSERT INTO ads VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (
            None,
            item['sale_rent'],
            item['apt_house'],
            item['city'],
            item['city_area'],
            item['price'],
            item['area'],
            item['year'],
            item['yard_area'],
            item['floor'],
            item['total_floors'],
            item['legalized'],
            item['heating'],
            item['rooms'],
            item['bathrooms'],
            item['url']
        ))
        self.conn.commit()
        return item
