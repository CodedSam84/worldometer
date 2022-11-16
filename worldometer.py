# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 23:08:51 2022

@author: swuma
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
	

url ="https://www.worldometers.info/world-population/"
page = requests.get(url).text
	

soup = BeautifulSoup(page, "lxml")
	

table = soup.find_all("table", class_ ="table table-striped table-bordered table-hover table-condensed table-list")[0]
	

all_rows = table.find_all("tr")
	

headers = table.find_all("th")
header_texts = []
	

for i in headers:
    title = i.text
    header_texts.append(title)
	    	

df = pd.DataFrame(columns=header_texts)
	

data_rows = all_rows[1:]
	

for j in data_rows:
	data_tags = j.find_all("td")
	data = [k.text for k in data_tags]
	length = len(df)
	df.loc[length] = data
	

df.to_csv("C:/Users/swuma/scrapping/worldometer.csv")

