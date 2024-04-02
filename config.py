import datetime

USER_STORAGE_URL = ''
AWS_SECRET_KEY = ''
AWS_PUBLIC_KEY = ''
date = '2024-04-02'
id = 0


def change_date():
    global date
    date = str(datetime.date.today())
    return date


def change_id():
    global id
    id +=1
    return id