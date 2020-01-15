import requests
import config
from bs4 import BeautifulSoup as BS
import mysql.connector

cnx = mysql.connector.connect(
  host=config.hostj,
  user=config.userj,
  passwd=config.pwj,
  database = 'nfl_draft_info')

cursor = cnx.cursor()

cursor.execute("""CREATE TABLE draft_picks(
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                pick_number INT,
                name VARCHAR(100),
                position VARCHAR(10),
                college VARCHAR(50),
                year INT
                )""")

def get_draft_info(year):
    draft_page = requests.get("https://www.pro-football-reference.com/years/" + str(year) + "/draft.htm")
    draft_soup = BS(draft_page.content, 'html.parser')
    draft_html = list(draft_soup.children)[3]
    draft_body = list(draft_html.children)[3]
    draft_table = list(draft_body.children)[1]
    draft_info = list(draft_table.children)[11]
    draft_info_table = list(draft_info.children)[9]
    draft_detail = list(draft_info_table.children)[3]
    dtable = draft_detail.find("table")
    drows = dtable.findAll('tr')
    ddata = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in drows]
    ddata2 = []
    for i in ddata:
        if len(i) == 28:
            ddata2.append({'pick': i[0], 'name': i[2], 'position': i[3], 'college': i[-2], 'year': year})
    return ddata2

def get_draft_list(year1, year2):
    draft_results_list = []
    for i in range(year1, year2):
        draft_results = get_draft_info(i)
        for sub in draft_results:
            for key in sub:
                sub[key] = str(sub[key]).strip("['']")
        for sub in draft_results:
            sub['pick'] = int(sub['pick'])
        for sub in draft_results:
            sub['year'] = int(sub['year'])
        draft_results_list.append(draft_results)
    return draft_results_list
def get_full_player_list(year1, year2):
    draft_results_ld = get_draft_list(year1, year2)
    draft_list = []
    for year in draft_results_ld:
        for player in year:
            draft_list.append((player['pick'], player['name'], player['position'], player['college'], player['year']))
    return draft_list
draft_list = get_full_player_list(2001,2020)

def insert_into_sql(dlist):
    stmt = "INSERT INTO nfl_draft_info.draft_picks (pick_number, name, position, college, year) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(stmt, dlist)
    cnx.commit()
insert_into_sql(draft_list)
