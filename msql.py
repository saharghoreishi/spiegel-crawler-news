import sqlite3


def Db(title, subtitle, abstract, date):
    conn = sqlite3.connect("sample.db")
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS Spiegeln (
         Title TEXT  NOT NULL,
         SubTitle TEXT  NOT NULL,
         Abstract TEXT  NOT NULL,
         InsertedDate VARCRCHAR(20)  NOT NULL)
         UNIQUE (Title, SubTitle, Abstract) ON CONFLICT IGNORE ''')
    except sqlite3.OperationalError as e:
        print('sqlite error:', e.args[0])  # table Spiegelnews already exists

    conn.commit()
    # if title[title.index[':'] + 1:len(title)] is not None:

    news = [title, subtitle, abstract, date]
    try:

        sql = '''INSERT OR REPLACE INTO Spiegeln (Title, SubTitle, Abstract, InsertedDate) VALUES ( ?, ?, ?, ?)'''
        c.execute(sql, news)
    except sqlite3.IntegrityError as e:
        print('sqlite error: ', e.args[0])  # column name is not unique

    conn.commit()
    conn.close()
