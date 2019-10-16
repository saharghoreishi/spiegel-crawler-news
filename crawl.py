import sqlite3
import spiegel

spiegel.Crawl()
conn = sqlite3.connect("sample.db")
c = conn.cursor()
sql = '''SELECT * FROM Spiegeln '''
for company in c.execute(sql):
    print(company)
conn.close()
