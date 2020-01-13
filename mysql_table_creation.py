import mysql.connector
import config
from mysql.connector import errorcode

#set database name
DB_NAME = 'nfl_draft_info'

#create connection
cnx = mysql.connector .connect(
    host = config.host,
    user = config.user,
    passwd = config.password,
    database = DB_NAME,
    use_pure=True
)

#start cursor
cursor = cnx.cursor()

TABLES = {}

TABLES['nfl_combine_info'] = (
"""CREATE TABLE nfl_combine_info (
    row_id int NOT NULL AUTO_INCREMENT,
    player varchar(40),
    year int,
    position varchar(10),
    school varchar(40),
    height varchar(100),
    weight int,
    40yd decimal(10,8),
    vertical decimal(10,8),
    bench int,
    broad_jump int,
    3cone decimal(10,8),
    shuttle decimal(10,8),
    pick_number int,
    PRIMARY KEY (row_id)
    );""")


#table creation function accepts a list and exectutes each element
def table_creation(table_list):
    for table_name in table_list:
        table_description = table_list[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

table_creation(TABLES)
