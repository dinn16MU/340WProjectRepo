import pandas as pd
import requests
from bs4 import BeautifulSoup


url = 'https://fbref.com/en/comps/9/2023-2024/playingtime/2023-2024-Premier-League-Stats'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

soup = str(soup).split('</div><div class="placeholder"></div>')[1].split('<div class="footer no_hide_long" id="tfooter_stats_shooting">')[0]

soup = soup.replace('<!--', '').replace('-->', '')

table = pd.read_html(str(soup))[0]

table.columns = table.columns.droplevel(0)

table = table[table['Rk'] != 'Rk']

table.to_csv('premier_league_playingtime_stats.csv', index=False)

print(table)