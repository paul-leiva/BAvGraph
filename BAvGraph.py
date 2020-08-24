from bs4 import BeautifulSoup
import requests
import matplotlib

print('Cody Bellinger')

response = requests.get('https://www.baseball-reference.com/players/b/bellico01.shtml')

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find("table", id='batting_standard')

rows = table.find_all('tr', attrs = {'class':'full'})
for row in rows:
    for cell in row.find_all('td'):
        print(cell.get_text())


tabledata = []

#posts = soup.find_all(class_="full")

#print(tabledata)
"""
for row in rows:
    target_column = row.find_all('td', 'right ')
    #target_column = row.find_all('attrs={"data-stat": "lg_ID"}')
    print(target_column)
"""