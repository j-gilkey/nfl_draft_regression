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
    add_row = ("""INSERT INTO nfl_combine_info_2
               (player, year, position, school, height, weight, forty_yd, vertical, bench, broad_jump, three_cone, shuttle, pick_number)
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
    update_row = ('UPDATE nfl_combine_info_2 SET ' +column_name+ ' = NULL WHERE '+column_name+' = 0;')
    print(update_row)

    cursor.execute(update_row)
    cnx.commit()

def get_all_combine_data():
    get_data = ('(SELECT *  FROM nfl_combine_info_2)')
    cursor.execute(get_data)
    return cursor.fetchall()

def get_joined_data():
    get_data = ('''SELECT sal.row_id
                ,sal.player
                ,sal.duration_years
                ,sal.total_value
                ,sal.initial_guaratees
                ,sal.total_gaurantees
                ,com.year
                ,com.position
                ,com.height
                ,com.weight
                ,com.forty_yd
                ,com.vertical
                ,com.bench
                ,com.broad_jump
                ,com.three_cone
                ,com.shuttle
                ,com.pick_number
            FROM nfl_draft_info.starting_salary sal
            INNER JOIN nfl_draft_info.nfl_combine_info_2 com ON(lower(sal.player) = lower(com.player));''')
    cursor.execute(get_data)
    return cursor.fetchall()

def update_salary_names(current_name, corrected_name):
    update_row = ('UPDATE starting_salary SET player = "'+corrected_name+'" WHERE player = "'+current_name+'";')
    print(update_row)

    #cursor.execute(update_row)
    #cnx.commit()


#update_salary_names("Adoree' Jackson", "Adoree Jackson")
