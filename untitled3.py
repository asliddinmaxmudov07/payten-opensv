# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E2HFivmWghXH52M4O3L0zUU0UJSpxeMq
"""

import pandas as pd
baza ={
   "FISH":["Qadamovi Zulayho","Xalilov Durbek", " Qurboniva  Gulnoza","Jo'rayeva Gulnoza" , "Djalilov Mamatisa", "Arabboyev Alisher"],
   "Manzil":["Farg'ona shahar ","Farg'ona shahar ","Qo'qon  ","Farg'ona shahar ","Qo'qon  ","Farg'ona shahar "],
   "Yoshi":["28","29","34","35.","65","68"],
   "ish joyi":["Tatuff","Tatuff", "Tatuff", "Tatuff", "Tatuff","Tatuff"],
   "Jinsi":["ayol","erkak","ayol","ayol","erkak", "erkak"],
}
db=pd.DataFrame(baza)
print (db)

filtr1=db[db['Jinsi']=="ayol"]
print (filtr1)

filtr2=db[(db["ish joyi"]=="Tatuff")&(db["Jinsi"]=="ayol")]
print (filtr2)