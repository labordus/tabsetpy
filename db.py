import sqlite3
import os
import appdirs
from diversen import *


def Initialize_db():
    returnvalue = True
    filepath = path_to_db()
    try:
        #        conn = sqlite3.connect(filepath, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conn = sqlite3.connect(filepath, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblApp(
                      appVERSION VARCHAR(7),
                      appFIRSTRUN BOOLEAN DEFAULT (1))''')
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblTabset(
                      tabsetID INTEGER PRIMARY KEY,
                      tabsetNM VARCHAR(20) UNIQUE NOT NULL,
                      tabsetOM VARCHAR(200),
                      tabsetSTAMP TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblURL(
                      urlID INTEGER PRIMARY KEY,
                      urlURL VARCHAR(200) UNIQUE NOT NULL,
                      urlNM VARCHAR(200) UNIQUE NOT NULL,
                      urlOM VARCHAR(200))''')
        c.execute('''CREATE TABLE IF NOT EXISTS
                      tblURLinfo(
                      tabsetID INTEGER REFERENCES tblTabset (tabsetID),
                      urlID INTEGER REFERENCES tblURL (urlID))''')
        conn.commit()
# geen record/row gevonden in tblApp
        c.execute('SELECT * FROM tblApp')
        data = c.fetchall()
        if len(data) == 0:
            c.execute('''INSERT INTO tblApp(appVERSION, appFIRSTRUN)
                    VALUES(?,?)''', (APP_VERSION, default_firstrun))
            conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
        returnvalue = False
    finally:
        conn.close()
    return returnvalue


def path_to_db():
    path = appdirs.user_data_dir('tabsetpy', False, False, False)
    check_path_exists(os.path.join(path, 'tabsetpy.db'))
    filepath = os.path.join(path, 'tabsetpy.db')
    return filepath


def check_path_exists(path):
    d = os.path.dirname(path)
    if not os.path.exists(d):
        os.makedirs(d)
