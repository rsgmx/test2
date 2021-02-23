import sqlite3

print("Hello world")

def somef():
    print("somef")

def c():
    sql = "create table IF NOT EXISTS pers( name varchar2(20) ) "
    with sqlite3.connect('test.db') as conn:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur = conn.cursor()
        sql2 = " insert into pers( name) values ( ?); "
        cur.execute(sql2, ["test4"] )
        cur.execute(sql2, ["test5"] )    
        conn.commit
        #connection.close()
        #connection = sqlite3.connect("test.db")
        cur3 = conn.cursor()
        cur3.execute("select * from pers")
        inhalt = cur3.fetchall()
        print(inhalt)

if __name__ == "__main__":
    print("main")
    c()