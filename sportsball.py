from psycopg2 import connect
from tabulate import tabulate


class sportsball:
    def __init__(self):
        self.conn, self.cur = self.connect_db()
        self.conn.commit()

        self.table_headers = ['jersey', 'name', 'pos',
                              'status', 'height','weight',
                              'bday', 'exp', 'college']

    #connect to default DB of PSQL
    def connect_db(self):
        try:
            conn = connect("dbname=sportsball user=SomeOne host=/tmp/")
        except:
            print("Unable to connect")

        return conn, conn.cursor()


    def create_table(self):
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
        self.cur.execute(create_table)

    def load_csv(self):
        self.cur.execute("COPY players(jersey, name, pos, status, height, weight, bday, exp, college) "
                    "FROM '/Users/Nic/TIY/W6/sports_ball/data/players.csv' DELIMITER',' CSV")

    def print_table(self):
        try:
            self.cur.execute("SELECT * from players")
        except:
            print("I can't SELECT from players")

        rows = self.cur.fetchall()
        temp = self.get_table_col()
        print(tabulate(rows, headers=temp, tablefmt='grid'))


    def print_table_col(self):
        self.cur.execute("SELECT * FROM players LIMIT 0;")
        self.colnames = [desc[0] for desc in self.cur.description]
        print('-'*138)
        for item in self.colnames:
            print("  |- {} -".format(item), end="| ")

    def get_table_col(self):
        self.cur.execute("SELECT * FROM players LIMIT 0;")
        return [desc[0] for desc in self.cur.description]

    def add_to_table(self):
        table_cols = self.get_table_col()
        len_table = len(table_cols)
        temp_list = []
        id = self.get_highest_id()
        temp_list.append(int(id)+1)
        for item in table_cols[1:]:
            print("Please input value for {} ".format(item))
            temp_list.append(input(">>> "))

        self.cur.execute("INSERT INTO players VALUES %r" %(self.lst2pgarr(temp_list)))

    def get_highest_id(self):
        self.cur.execute("SELECT id FROM players "
                         "ORDER BY id DESC LIMIT 1;")

        rows = self.cur.fetchall()
        return rows[0][0]

    def get_last_row(self):
        self.cur.execute("SELECT * FROM players "
                         "ORDER BY id DESC LIMIT 1")
        rows = self.cur.fetchall()
        print(rows)

    def lst2pgarr(self, alist):
        temp_list = []
        for item in alist:
            temp = str(item)
            temp_list.append(temp)
        temp_str =  '{' + ','.join(temp_list) + '}'
        return temp_str

    def close_db(self):
        self.cur.close()
        self.conn.close()



if __name__ == '__main__':
    f = sportsball()
    f.create_table()
    f.load_csv()
    # f.get_table_col()
    # f.print_table()
    f.add_to_table()
    f.get_last_row()
    f.close_db()




