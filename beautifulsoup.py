from bs4 import BeautifulSoup
import urllib.request
import requests
import re
from selenium import webdriver
import datetime
import os
import telegram

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.22 Safari/537.36'}

def create_soup(url):
  result = requests.get(url, headers=headers)
  result.raise_for_status()
  soup = BeautifulSoup(result.text, "lxml")
  return soup