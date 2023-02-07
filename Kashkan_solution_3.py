#!/usr/bin/python3
import re
from urllib.request import urlopen

def hockey_scrapper(team='Olomouc'):
    """ Without BeautifullSoup this task is quite cruel,
    but ok.. regex will help us then
    
    BTW. In the output example you show there is a mistake - 
    Kometa lost two times, once to Trinec and once to Plzen

    Args:
        team (str, optional): team to select. Defaults to 'Olomouc'.
    """
    
    # Uploading the page
    url = "https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    
    # extracting values
    # extracting date of game
    pattern_1 = re.compile(r"(?<=\"datetime-container\">)(\d+\.\s\d+\.)")
    all_dates = [x.replace(u'\xa0', ' ') for x in re.findall(pattern_1, html)]
    # extracting loosers
    pattern_2 = re.compile(r'(?<=\"team-name team-looser\">)(\w+)')
    all_loosers = re.findall(pattern_2, html)
    # extracting winners
    pattern_3 = re.compile(r'(?<=\"team-name\">)(\w+)')
    all_winners = re.findall(pattern_3, html)
    games_list = list(zip(all_dates, all_loosers, all_winners))
    
    # Input check:
    if (team_name not in all_loosers) and (team_name not in all_loosers):
        raise NameError('Team with such name haven\'t played this season')
    
    for game in games_list:
        if team == game[-1]:
            print(f"{game[0]} we won over {game[1]}")
        elif team == game[1]:
            print(f"{game[0]} we were bitten by {game[-1]}")
        else:
            pass

if __name__ == "__main__":
    team_name = input("Enter the team name: ")
    hockey_scrapper(team_name)

        
    