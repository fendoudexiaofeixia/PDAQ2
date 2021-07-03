# config = UTF-8
import pymysql

user = 'root'
password = 'calmcar'
host = '192.168.196.220'
port = 3306
database = 'PDAQ'


class connect:
    def __init__(self):
        self.db = pymysql.connect(user=user, password=password, host=host, port=port, database=database)
        self.cur = self.db.cursor()

    def execute(self, sql):
        self.cur.execute(sql)

    def comm(self):
        self.db.commit()

    def shutdown(self):
        self.cur.close()
        self.db.close()


def update_data():
    con_mysql = connect()
    getdata_sql = "SELECT * FROM my_app_pdaq"
    con_mysql.execute(getdata_sql)
    con_mysql.comm()
    res = con_mysql.cur.fetchall()
    for i in res:
        print(i)


if __name__ == '__main__':
    update_data()
