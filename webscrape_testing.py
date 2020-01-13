import requests
from bs4 import BeautifulSoup
import mysql_functions as my_funcs


def imdb_season_1_scraper(id_list):

    for id in id_list:
        if id_list.index(id)%10 == 0:
            print("on show number " + str((id_list.index(id) + 1)) )
        page = requests.get("https://www.imdb.com/title/" + str(id[0]) +  "/episodes?season=1")
        soup = BeautifulSoup(page.content, 'html.parser')
        list = soup.find_all(class_="ipl-rating-star small")
        #get all outer classes containing the rating and vote counts

def create_tuple(player, year, stats, pick):
    new_list = []
    del stats[2]
    new_list.append(player[0])
    new_list.append(year)
    for stat in stats:
        new_list.append(stat)
    new_list.append(pick)
    new_tuple = tuple(new_list)
    return new_tuple


def nfl_year_scrape(year):

    page = requests.get("https://www.pro-football-reference.com/draft/" + str(year) + "-combine.htm")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table')
    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        th = tr.find_all('th')
        header = list([i.text for i in th])
        row = list([i.text for i in td])
        if row:
            final = row.pop()
            #print(final)
            if final:
                #pick = final.split(' / ')
                pick = str(final.split(' / ')[2]).strip('pick thsnrd')
                #print(pick)
            else:
                pick = ''
        else:
            pick = ''
        #print(row)
        if len(row) == 11:
            data_tuple = create_tuple(header,year, row, pick)
            my_funcs.insert_combine_year(data_tuple)
            # print(len(data_list))
            # print(data_list)


    print(page)

nfl_year_scrape(2000)
