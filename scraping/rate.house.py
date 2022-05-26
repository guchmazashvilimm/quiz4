import requests
from bs4 import BeautifulSoup
file = open('movies.csv','w',encoding='utf-8_sig')
def rate_house(page_number):
    url = 'https://rate.house/chart/movie/?capVal=965&orderBy=rating&fromYear=0&toYear=2022&tags=&pageNum='+str(page_number)
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    wrapper = soup.find('div', class_='wrapper')
    section = wrapper.find('div', class_='box-section')
    relations = section.find('div', class_='relations')
    relation = relations.find_all('div', class_='relation')
    for each in relation:
        info = each.find('div', class_='item-info')
        rating = info.find('div', class_='rating-info')
        rate_div = rating.find('div', class_='relation-extra')
        rate = rate_div.text
        title = (rating.a.text).strip()
        year = (rating.span.text).strip()
        file.write(title + "-" + year+ "\n"+ rate +'\n' +"\n")

for i in range(1,6):
    rate_house(i)