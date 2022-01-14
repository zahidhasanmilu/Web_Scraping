import scrapy
import csv

class Bot2Spider(scrapy.Spider):
    name = 'Bot2'
    allowed_domains = ['https://www.monsterindia.com/']
    start_urls = []
    with open('Job_Skills_Links.csv', mode='r', newline='', encoding='utf-8')as f:
        reader = csv.reader(f)
        start_urls = [link[0] for link in reader]
    start_urls = start_urls[0:3] #website pages

    def parse(self, response):
        titles = response.xpath(
            '//*[@id="srp-jobList"]/div/div/div/div[1]/div/div/h3/a/text()').getall()

        companies = response.xpath(
            '//*[@id="srp-jobList"]/div/div/div/div[1]/div/div/span/a/text()').getall()

        locations = response.xpath(
            '//*[@id="srp-jobList"]/div/div/div/div[1]/div/div/div/div[1]/span/small/text()').getall()
        locations = list(map(lambda data: data.strip() if data else "NA", locations))
        
        exp = response.xpath(
            '//*[@id="srp-jobList"]/div/div/div/div[1]/div/div/div/div[2]/div/span/small').getall()
        exp = list(map(lambda data: data.split('\n')[
                   2].strip() if data else "NA", exp))

        salary = response.xpath(
            '//*[@id="srp-jobList"]/div/div/div/div[1]/div/div/div/div[3]/span/small/text()').getall()
        salary = list(map(lambda data: data.strip() if data else "NA", salary))

        description = response.xpath(
            '//*[@id="srp-jobList"]/div/div/div/div[1]/div/p[1]/text()').getall()
        description = list(map(lambda data: data.strip()
                           if data else "NA", description))

        data = []
        for index in range(25):
            data.append([
                titles[index], companies[index], locations[index], exp[index], salary[index], description[index]
            ])
        
        with open('JobData.csv', mode='w', newline='', encoding='utf-8')as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Companie', 'Location', 
                            'Exeprience', 'Salary', 'Description'])
            writer.writerows(data)
        

