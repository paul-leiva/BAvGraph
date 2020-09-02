from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import sys

while True:
    try:

        player_name = input('\nEnter Player Name (Ex: Babe Ruth): ')
        if (player_name == 'quit'):
            sys.exit()
        player_name = player_name.lower()
        player_name = player_name.split()
        first_name = player_name[0]
        last_name = player_name[1]

        url = 'https://www.baseball-reference.com/players/'
        url += last_name[0:1] + '/' + last_name[:5] + first_name[:2] + '01.shtml'

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        realName = soup.find("h1", attrs = {'itemprop':'name'}).get_text()
        print(realName)

        table = soup.find("table", id='batting_standard')
        rows = table.find_all('tr', attrs = {'class':'full'})

        prevYear = 0
        data = []
        yrs = []
        avgs = []
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
            data.append([Year, Team, League, float(BA), HR])
            yrs.append(Year)
            avgs.append(float(BA))
        graph, axis = plt.subplots()
        plt.ylim(0, .500)
        plt.xlabel("Season")
        plt.ylabel("Batting Average")
        plt.title(realName)
        axis.grid(True)
        axis.scatter(yrs, avgs, color='r', edgecolors='black')
        axis.plot(yrs, avgs, color='gray')  # add a line to connect the dots
        plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%.3f'))
        plt.show(block=False)
        plt.show()
    except:
        print('ERROR: Player data could not be fetched. Try a different player.')