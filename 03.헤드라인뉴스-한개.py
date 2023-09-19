import requests
from bs4 import BeautifulSoup


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
response = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100" , headers = header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('.sh_text_headline')
print(title.text.strip())
