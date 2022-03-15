import time
from bs4 import BeautifulSoup
from selenium import webdriver  # 從library中引入webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import soup

driver = webdriver.Chrome()  # 開啟chrome browser

from selenium.webdriver.support.ui import Select

driver.get(
    "https://land-query.tainan.gov.tw/query/rwd/noncityland.jsp?csrf.param=01D5660154534A1C7F4AB4B61C2AF2F2&menu=false#queryResult"
)  # 更改網址以前往不同網頁

for a in soup.article:

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "NUM1"))
    )

    search.clear
    search.send_keys("0985")



    ele = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "SiteArea"))
    )

    select = Select(ele)
    select.select_by_visible_text(a.text)

    time.sleep(0.5)

    ele2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "R48check"))
    )


    select2 = Select(ele2)
    # select2.select_by_visible_text("南社內段")


    link = driver.find_element_by_name("button1")

    link.click()

    spc1 = driver.find_element_by_xpath(
        '//*[@id="queryResult"]/div[2]/div/table/tbody/tr/td[4]'
    )
    print(spc1.text)

    spc2 = driver.find_element_by_xpath(
        '//*[@id="queryResult"]/div[2]/div/table/tbody/tr/td[5]'
    )
    print(spc2.text)



