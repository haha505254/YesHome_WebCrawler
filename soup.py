import requests


from bs4 import BeautifulSoup
html_doc  = requests.get(
 "https://land-query.tainan.gov.tw/query/rwd/noncityland.jsp?csrf.param=01D5660154534A1C7F4AB4B61C2AF2F2&menu=false#queryResult"
)


soup = BeautifulSoup(html_doc.text, 'html.parser')
tag_name = 'select.textfield.form-control option'
# print(soup.select(tag_name))

for article in soup.select(tag_name):
    print(article.text)
