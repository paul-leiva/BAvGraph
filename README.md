# BAvGraph
 A program that graphs a baseball player's batting average (BA over the course of their career. (Pronounced *BAV-graph*)
 
## Libraries You Will Need to Install:
- BeautifulSoup (`pip install beautifulsoup4`)
- requests (`pip install requests`)
- matplotlib (`pip install matplotlib`)
You will also need the `sys` library, but this comes standard with Python.
<br>**NOTE**: In order to install BeautifulSoup and for this program to work, you **MUST** be using a version of Python3. If you are using Python2, this program will probably not work.

## How this Program Works:
1. The user will be prompted to enter a player's name (Ex: Babe Ruth) from the console/terminal.
2. Using the `requests` and `BeautifulSoup` libraries, the player is found on baseball-reference.com. Baseball Reference uses a standard URL convention to identify players by name. If the player is not found or the player's page is erroneous when fetching is attempted, the process is exited and the user will be prompted to enter a different player name.
3. For the player's *Standard Batting* table, the player's batting average in every Major League season/year is fetched. If you look on the player's actual webpage, you will see there may be multiple entries for 1 season for players who were traded or were released and re-signed in a single season. However, this program deals with that and only collects the cumulative/total average for every season even if the player was with multiple teams. Pre-season, minor league, all-star game, and postseason batting is NOT included in this fetching.
4. The averages for each season are then plotted on a scatter plot for the player.
5. To search for another player, click the "Close Window" button (the red 'X' in the upper left of the window on Mac device) and then you should be prompted to search for another player after that.

## How to Input a Player Name:
![UserInput](/UserInput.png?raw=true)
When inputting a player name, this program only works with the players "on-field" name. Full names, nicknames, previous names for players who have changed their names, etc. will not work. Some examples of player names include `Babe Ruth`, `Lou Gehrig`, `David Ortiz`, `Giancarlo Stanton`, and `Mike Trout`. For players with special characters in their name (ñ, ü, accented vowels, etc.), **DO NOT** type those special characters. The URLs are not written with special characters, so your player data will not be fetched. Instead, just type the normal letter. (Ex: To search for Carlos Peña, you would type `Carlos Pena` and it will find him.)

## What Your Ouput will look like:
![SampleGraph](/SampleGraph.png?raw=true)

## Know Issues and Bugs:
1. Players known by intials may or may not be found due to the way their URL is formatted by Baseball-Reference (Ex: JB Shuck, J.D. Martinez, etc.). Most of these players who go by initials seem to be able to be found in normal fashion. However, some are not.
2. Players with the same name as other players (Ex: the Billy Hamilton's) cannot be discerned by this program.
3. Father & son players also cannot be distinguished from each other (Ex: Ken Griffey Sr./Jr.).
4. For players who played in the league for a while (15+ seasons), their graphs may show up bunched up with the years overlapping. You will have to expand the scatter plot's window to counteract this. It should display find after doing that.
5. Pitchers' batting data is not displayed in the same fashion as position players. So you will not be able to find pitchers' hitting data. Use this only for **position players.**
6. Some players with differently formatted web pages than the usual exist at random and will not display. However, this is a very small fraction of all players.
