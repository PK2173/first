# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.ndtv.com/latest")

    


# from lib2to3.pgen2 import driver
import json
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# chrome_option=webdriver.ChromeOption()
driver=webdriver.Chrome("./chromedriver")
driver.maximize_window()
driver.get("https://www.ndtv.com/latest")
# driver.find_element_by_xpath('//*[@id="inkmob-nav"]/li[2]/a').click()
# driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div[3]/article/div/div/div/div[1]/div/div[1]/div[2]/h2/a').click()
# sleep(7)
# pr=driver.find_element_all_by_xpath('/html/body/div[2]/div/div/section/div[2]/div[1]/h1')
# print(pr.text)
fer=driver.find_elements_by_xpath('/html/body/div[2]/div/div/section/div[3]/article/div/div/div/div[1]/div')
details={}
cout=1
for i in fer:
    details[cout]=i.text.strip()
    cout+=1
    print()
    # print(i.text)
with open('main.json','w') as d:
    json.dump(details,d,indent=4)