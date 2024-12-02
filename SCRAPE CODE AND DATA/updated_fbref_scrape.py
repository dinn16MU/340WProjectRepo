import pandas as pd
import requests
from bs4 import BeautifulSoup

#data_type = ["stats","passing","passing_types","gca","defense","possession","playingtime","misc"]


#for i in data_type: 

url = f'https://fbref.com/en/comps/Big5/2023-2024/shooting/players/2023-2024-Big-5-European-Leagues-Stats'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

soup = str(soup).split('</div><div class="placeholder"></div>')[1].split('<div class="footer no_hide_long" id="tfooter_stats_shooting">')[0]

soup = soup.replace('<!--', '').replace('-->', '')

table = pd.read_html(str(soup))[1]

table.columns = table.columns.droplevel(0)

table = table[table['Rk'] != 'Rk']

table.to_csv(f'Big-5-European-Leagues-Stats_shooting_stats.csv', index=False)


#stats
#shooting
#passing
#passing_types
#gca
#defense
#possession
#playingtime
#misc