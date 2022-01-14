import scrapy
import csv 

class Bot1Spider(scrapy.Spider):
    name = 'Bot1'
    allowed_domains = ['https://www.monsterindia.com/']
    start_urls = ['https://www.monsterindia.com/search/jobs-by-skill']

    def parse(self, response):
        links = response.css('.ar-link::attr(href)').getall()

        #Writing Data in csv file
        with open('Job_Skills_Links.csv', mode='w', newline='', encoding='utf-8')as f:
            writer = csv.writer(f)
            writer.writerows([[link,]for link in links])