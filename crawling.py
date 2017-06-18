import configparser
import requests
import time

from pdfminer.pdfdocument import PDFTextExtractionNotAllowed
from requests.auth import HTTPBasicAuth

from selenium import webdriver
from selenium.webdriver.support.ui import Select  # for <SELECT> HTML form

from thesis import Thesis
import pickle

import requests
from bs4 import BeautifulSoup

# def download_pdf(url, cook, name):
#     response = requests.get(url, stream=True, cookies=cook)
#     with open('./data/' + name + '.pdf', 'wb') as fd:
#         fd.write(response.content)

# def get_info_page(driver, cook):
#     for row in driver.find_elements_by_css_selector('tr')[1:]:  # first one is header
#         thesis = extract_info_row(row)
#         print(thesis.name_thesis)
#         print(thesis.thesis_url)
#         download_pdf(thesis.thesis_url, cook, thesis.name_thesis)


# def main(config):
#     # driver = webdriver.PhantomJS()
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--incognito")

#     driver = webdriver.Chrome(chrome_options=chrome_options)
#     driver.implicitly_wait(10)  # seconds

#     driver.get("https://is.fit.cvut.cz/group/intranet/zp/list")

#     # Fill the login form and submit it
#     driver.find_element_by_id('username').send_keys(config["login"]["username"])
#     driver.find_element_by_id('password').send_keys(config["login"]["password"])
#     driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/button').click()

#     # For downloading pdf
#     cook = {i['name']: i['value'] for i in driver.get_cookies()}

#     get_info_page(driver, cook)

#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="A6323:resultTable:j_idt48:1:j_idt50"]').click()
#     get_info_page(driver, cook)

#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="A6323:resultTable:j_idt48:2:j_idt50"]').click()

#     get_info_page(driver, cook)

#     while True:
#         time.sleep(2)
#         driver.find_element_by_xpath('//*[@id="A6323:resultTable:j_idt48:3:j_idt50"]').click()

#         get_info_page(driver, cook)

def main2():


    def crawler(seed, limit = 1000):
        frontier = [seed]
        crawled = []
        theses = [] 
        while len(frontier) != 0 :
            page = frontier.pop()
            #try:
            print('Crawled:' + page)
            source = requests.get('https://dip.felk.cvut.cz/browse/' + page, verify=False)
            soup = BeautifulSoup(source.text.encode('iso-8859-1'), "lxml")

            if len(theses) % 30 == 1:
                print("SAVING ", len(theses))
                with open("data/data.plk", mode="wb") as file:
                    pickle.dump(theses, file)

            #print (soup.select("body > p > table > tbody > tr:nth-of-type(10) > td:nth-of-type(2)"))
            # on thesis page - no need to crawl links on this page
            if "details" in page: 
                thesis = {}
                for elem in soup.find_all('tr')[1:10]:
                    # print (elem)
                    title = elem.find_all('td')[0].get_text()
                    data = elem.find_all('td')[1].get_text()
                    #print ("title" + title + " data:" +data)
                    thesis[title] = data
                theses.append(thesis)
            # on non thesis page
            else:
                links = soup.findAll('a', href=True)

                if page not in crawled:
                    for link in links:
                        if ".." not in link["href"] and ".pdf" not in link['href'] and link['href'] not in crawled:
                            frontier.append(link['href'])
                    crawled.append(page)

            # except Exception as e:
            #     print(e)
        return

    crawler('', 50)



if __name__ == "__main__":
    #config = readConfig()
    # main(config)
    main2()
