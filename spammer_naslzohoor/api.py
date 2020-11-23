import pyautogui as py
import time as t
import sqlite3 as db
from colorama import init,AnsiToWin32,Back,Fore
import sys

con = db.connect('data.db')
c = con.cursor()

init(wrap=False)
color = AnsiToWin32(sys.stderr).stream

def append(txt):
    with open('data.txt','a') as text:
        text.write('{}\n'.format(txt))
def set_time(time):
    c.execute('''CREATE TABLE IF NOT EXISTS data (
    time integer
    )''')
    time1 = int(time)
    c.execute('INSERT INTO data VALUES (:time)',{'time':time1})
    con.commit()
    con.close()

def spam():
    c.execute('SELECT time FROM data')
    time = str(c.fetchone())
    time1 = time.replace('(','',5)
    time2 = time1.replace(')','',5)
    time3 = time2.replace(',','',5)
    time4 = int(time3)
    t.sleep(time4)
    py.FAILSAFE = False
    txt = open('data.txt','r')
    for i in txt:
        py.typewrite(i)
        py.press('enter')
        print(Fore.GREEN,'[+] Send')
    txt.close()
