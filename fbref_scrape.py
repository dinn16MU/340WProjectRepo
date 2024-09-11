import pandas as pd
import requests
from bs4 import BeautifulSoup


response = requests.get('https://fbref.com/en/comps/9/stats/Premier-League-Stats')
txt = response.text.replace('<!--', '').replace('-->', '')


table = pd.read_html(txt)[-1]
table.columns = table.columns.droplevel(0)
table = table[table['Rk'] != 'Rk']