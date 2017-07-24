from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 9999)
suki = client['suki']
url_list = suki['url_list']


# spider1爬取所有商品链接
def get_links_from(channel, pages, who_sells=0):
    # http://bj.58.com/diannao/pn2/
    list_view = '{}{}/pn{}/'.format(channel, str(who_sells), str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('td','t'):
    for link in soup.select('td.t a.t'):
        item_link = link.get('href').split('?')[0]
        url_list.insert_one({'url': item_link})
        print(item_link)
    else:
        pass
    #nothing

def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    title = soup.title.text
    price =


get_links_from("http://bj.58.com/bijiben/", 2)
