from bs4 import BeautifulSoup
import requests 
import re
from selenium import webdriver
import time
# BeautifulSoup 객체만들기
def create_soup(url):
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36')

}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def scrape_share_price():
    print('[[ 오늘의 주식]]')
    res = requests.get('https://finance.naver.com/sise/sise_market_sum.naver')
    soup = BeautifulSoup(res.content,'html.parser')

    section = soup.find('tbody')
    items= section.find_all('tr', onmouseover="mouseOver(this)")
    for item in items :
        basic_info = item.get_text()
        sinfo = basic_info.split("\n")
        print("\t" + sinfo[1] +"\t\t"+sinfo[2]+"\t\t\t"+sinfo[3])

if __name__=='__main__':
    scrape_share_price()