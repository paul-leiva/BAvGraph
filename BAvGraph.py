from bs4 import BeautifulSoup
import requests
import matplotlib

print('Kenny Lofton')
response = requests.get('https://www.baseball-reference.com/players/l/loftoke01.shtml')

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
    print(Year + '|' + Team + '|' + League + '|' + HR + '|' + BA)
    #for cell in row.find_all('td'): FROM EVERY ROW
        #print(cell.get_text())      PRINT EVERY CELL

print(data)
