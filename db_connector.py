import sqlite3

def add(text: str):
    try:
        con = sqlite3.connect("/home/a/bots/purchases/app.db")
        cursor = con.cursor()
        cursor.execute('''insert into list values(?)''', (str(text),))
        con.commit()    
        con.close()
    except Exception as e:
        return e
    return 'good'

def delete(text: str):
    try:
        con = sqlite3.connect("/home/a/bots/purchases/app.db")
        cursor = con.cursor()
        cursor.execute('''delete from list where date=?''', (str(text),))
        con.commit()    
        con.close()
    except Exception:
        return 'error'
    return 'good'

def getList():
    try:
        con = sqlite3.connect("/home/a/bots/purchases/app.db")
        cursor = con.cursor()
        cursor.execute('''select * from list''')
        answer = cursor.fetchall()
        con.close()
        tmp = []
        for i in answer:
            tmp.append(i[0])
        return tmp
    except Exception as e:
        print(e)
        return e