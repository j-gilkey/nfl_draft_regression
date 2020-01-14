import requests
from bs4 import BeautifulSoup
import mysql_functions as my_funcs

def create_tuple(player, year, stats, pick):
    #puts player, year, stats and pick into a list where stats is alreay a list
    new_list = []
    del stats[2]
    new_list.append(player[0])
    new_list.append(year)
    for stat in stats:
        new_list.append(stat)
    new_list.append(pick)
    new_tuple = tuple(new_list)
    return new_tuple


def combine_year_scrape(year):
    #takes in a year and scrapes in order to get NFL combine info and draf pick rank for each rookie in that year
    page = requests.get("https://www.pro-football-reference.com/draft/" + str(year) + "-combine.htm")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table')
    table_rows = table.find_all('tr')

    tuple_list = []

    for tr in table_rows:
        td = tr.find_all('td')
        th = tr.find_all('th')
        header = list([i.text for i in th])
        row = list([i.text for i in td])
        if row:
            split_row = row[3].split('-')
            split_sum = (int(split_row[0])*12) + int(split_row[1])
            #print(row)
            row[3] = split_sum
            #print(row)
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
            tuple_list.append(data_tuple)
            #my_funcs.insert_combine_year(data_tuple)
            # print(len(data_list))
            # print(data_list)

    return tuple_list

#combine_year_scrape(2005)

def combine_year_paginate():
    #loops through each year between 2000 and 2019
    years = list(range(2000,2020))
    for year in years:
        year_tuples = combine_year_scrape(year)
        print(year)
        my_funcs.insert_combine_year(year_tuples)

def clear_zeroes():
    #goes through each of the columns in the column list and replaces zero values with NULL
    column_list = ['40yd', 'vertical', 'bench', 'broad_jump', '3cone', 'shuttle', 'pick_number']

    for column_name in column_list:
        my_funcs.change_zero_to_nan(column_name)
        #print(column_tuple)

clear_zeroes()

#combine_year_paginate()
