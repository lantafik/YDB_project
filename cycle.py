import time
import schedule
import config

schedule.every().day.at("05:00").do(config.change_date)

print(config.date)
while True:
    schedule.run_pending()
    time.sleep(1)
