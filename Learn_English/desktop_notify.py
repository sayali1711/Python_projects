import time
from random_word import RandomWords
from plyer import notification
from PyDictionary import PyDictionary
import random
import schedule

def learn_english():    
    with open("words.txt", "r") as file:
       allText = file.read()
       words = list(map(str, allText.split()))
       r=random.choice(words)

    title=r    
    dictionary=PyDictionary()
    msg=str(dictionary.meaning(title))
    notification.notify(title=title,message=msg,app_icon=None,timeout=5,toast=False)

schedule.every().hour.do(learn_english)
while True:
    schedule.run_pending()
    time.sleep(1)
