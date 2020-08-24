from bs4 import BeautifulSoup
import requests
import matplotlib

url = 'https://www.baseball-reference.com/players/'

name = input('Enter Player Name (Ex: Babe Ruth): ')
name = name.lower()
name = name.split()
first_name = name[0]
last_name = name[1]

print(last_name[:6] + first_name[:2])

url += last_name[0:1] + '/' + last_name[:6] + first_name[:2] + '01.shtml'
print(url)

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find("table", id='batting_standard')
rows = table.find_all('tr', attrs = {'class':'full'})

prevYear = 0
data = []
for row in rows:
    Year = row.find('th', attrs={"data-stat":"year_ID"}).get_text()
    if Year == prevYear:
        pass
    else:
        prevYear = Year
    Team = row.find('td', attrs={"data-stat":"team_ID"}).get_text()
    League = row.find('td', attrs={"data-stat":"lg_ID"}).get_text()
    BA = row.find('td', attrs={"data-stat":"batting_avg"}).get_text()
    HR = row.find('td', attrs={"data-stat": "HR"}).get_text()
    data.append([Year, Team, League, BA, HR])
    print(Year + '|' + Team + '|' + League + '|' + BA + '|' + HR)

print(data)
