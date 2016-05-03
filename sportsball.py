from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#connect to default DB of PSQL
try:
    conn = connect("dbname=sportsball user=SomeOne host=/tmp/")
except:
    print("Unable to connect")

cur = conn.cursor()

create_table = ("CREATE TABLE players(id serial PRIMARY KEY NOT NULL, "
                "jersey integer, "
                "name TEXT NOT NULL, "
                "pos TEXT, "
                "status TEXT, "
                "height INT, "
                "weight INT,"
                "bday date,"
                "exp INT,"
                "college TEXT); ")


cur.execute(create_table)
cur.execute("COPY players(jersey, name, pos, status, height, weight, bday, exp, college) FROM '/Users/Nic/TIY/W6/sports_ball/data/players.csv' DELIMITER',' CSV")
# cur.execute("FROM '/Users/Nic/TIY/W6/sports_ball/data/players.csv' DELIMITER',' WITH CSV")

try:
    cur.execute("""SELECT * from players""")
except:
    print("I can't SELECT from players")

rows = cur.fetchall()
print("\nRows: \n")
for row in rows:
    print("   ", row[2])

cur.close()
conn.close()

