import requests
from bs4 import BeautifulSoup


def imdb_season_1_scraper(id_list):

    for id in id_list:
        if id_list.index(id)%10 == 0:
            print("on show number " + str((id_list.index(id) + 1)) )
        page = requests.get("https://www.imdb.com/title/" + str(id[0]) +  "/episodes?season=1")
        soup = BeautifulSoup(page.content, 'html.parser')
        list = soup.find_all(class_="ipl-rating-star small")
        #get all outer classes containing the rating and vote counts

def create_list(player, stats):
    new_list = []
    new_list.append(player[0])

    for stat in stats:
        new_list.append(stat)
    return new_list


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
        print(create_list(header, row))

    print(page)

nfl_year_scrape(2017)
