import mysql.connector
import config

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

def insert_combine_year(combine_tuples):
    add_row = ("""INSERT INTO nfl_combine_info
               (player, year, position, school, height, weight, 40yd, vertical, bench, broad_jump, 3cone, shuttle, pick_number)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""")

    cursor.executemany(add_row, combine_tuples)
    cnx.commit()

def insert_salary_year(salary_tuples):
    add_row = ("""INSERT INTO starting_salary
               (player, duration_years, total_value, initial_guaratees, total_gaurantees)
               VALUES (%s, %s, %s, %s, %s);""")

    cursor.executemany(add_row, salary_tuples)
    cnx.commit()


def change_zero_to_nan(column_name):
    update_row = ('UPDATE nfl_combine_info SET ' +column_name+ ' = NULL WHERE '+column_name+' = 0;')
    print(update_row)

    cursor.execute(update_row)
    cnx.commit()

def get_all_combine_data():
    get_data = ('(SELECT *  FROM nfl_combine_info)')
    cursor.execute(get_data)
    return cursor.fetchall()
