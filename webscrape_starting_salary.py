import requests
import config
from bs4 import BeautifulSoup
import mysql_functions as my_funcs

def spotrac_year_scrape(year):
    page = requests.get("https://www.spotrac.com/nfl/contracts/type-rookie/signed-"+ str(year) +"/")
    soup = BeautifulSoup(page.content, 'html.parser')
    spot_table = soup.find('table')
    spotrows = spot_table.findAll('tr')
    spot_data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in spotrows]
    player_list = []
    i = 1
    while i < (len(spot_data) - 2):
        player = spot_data[i]
        player_tuple = (str(player[0][1]), year, str(player[4][0]), player[5][0].strip('$').replace(',',''), player[7][0].strip('$').replace(',',''), player[8][0].strip('$').replace(',',''))
        #print(player_tuple)
        player_list.append(player_tuple)
        i += 1
    return player_list

def spotrac_paginate():
    years = [2015,2016,2017,2018,2019]

    for year in years:
        player_list = spotrac_year_scrape(year)
        print(player_list[0])
        for item in player_list[0]:
            print(type(item))
        my_funcs.insert_salary_year(player_list)

#spotrac_paginate()

def clean_names():
    sal_com_no_match = {"Adoree' Jackson": "Adoree Jackson", "William Jackson": "William Jackson III",
             "Vernon Hargreaves": "Vernon Hargreaves III", "Lac Edwards": "Lachlan Edwards", "Garett Bolles": "Garrett Bolles",
             "Tre'Davious White": "TreDavious White" , "Julie'n Davenport": "Julien Davenport",
                   "Deatrich Wise": "Deatrich Wise Jr.", "Christopher Carson": "Chris Carson",
                   "Da'Ron Payne": "Daron Payne", "Ronald Jones II": "Ronald Jones", "Jessie Bates III": "Jessie Bates",
                   "DJ Chark": "D.J. Chark", "Orlando Brown Jr.": "Orlando Brown", "Tre'quan Smith": "Trequan Smith",
                   "Chuks Okorafor": "Chukwuma Okorafor", "Da'shawn Hand": "Dashawn Hand",
                    "Shaun-Dion Hamilton": "Shaun dion Hamilton", "Olasunkanmi Adeniyi": "Ola Adeniyi",
                   "Benny Snell Jr.": "Benny Snell", "Iman Marshall": "Iman Lewis-Marshall",
                   "Olabisi Johnson": "Bisi Johnson", "D’Cota Dixon":"D'Cota Dixon"}
    for key in sal_com_no_match:
        current_name = key
        corrected_name = sal_com_no_match[key]
        my_funcs.update_salary_names(current_name, corrected_name)
        print([current_name, corrected_name])

#clean_names()
