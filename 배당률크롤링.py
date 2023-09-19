import requests
from bs4 import BeautifulSoup


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
response = requests.get("https://www.wisetoto.com/index.htm?tab_type=toto&game_type=sc&game_category=sc1&game_year=2023&game_round=53&focus=369993_1" , headers = header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('.dividend')
print(title)
