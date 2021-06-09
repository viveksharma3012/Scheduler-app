import time
from plyer import notification
import pandas as pd
import random


df=pd.read_csv('C:\\Users\\sharm\\Desktop\\My Projects\\Scheduler app\\Word lists in csv\\fword.csv')

if __name__== "__main__":
   while(True):
      notification.notify (
      title = "Hydrate Yourself",
      message= str(df.iloc[random.randrange(10,5000)]),
      #app_icon= "C:\Users\sharm\Desktop\My Projects\Scheduler app\watericon.ico",
      timeout=7
      )
      time.sleep(90*60)   
