import sqlite3
import spiegel
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(spiegel.Crawl(), trigger='cron', second=60)


conn = sqlite3.connect("sample.db")#to see what inserted in sqllite
c = conn.cursor()
sql = '''SELECT * FROM Spiegeln '''
for company in c.execute(sql):
    print(company)
conn.close()
