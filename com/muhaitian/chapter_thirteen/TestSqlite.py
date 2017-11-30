import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE food(
        id  TEXT PRIMARY KEY,
        desc TEXT,
        water FLOAT,
        kcal FLOAT,
        protein FLOAT,
        fat FLOAT,
        ash FLOAT,
        carbs FLOAT,
        fiber FLOAT,
        sugar FLOAT
    )''')


def search(sql):
    curs.execute(sql)
    curs.commit()
