#!/usr/bin/env python3

from selenium import webdriver
import json

users={}
with open('users.json', 'r') as outfile:
     users=json.load(outfile)
driver=webdriver.Firefox()

driver.get('http://'+users['username']+':'+users['password']+'@192.168.1.234')
driver.switch_to.frame('child_page')
driver.find_element_by_id('webdata_now_p')
e=driver.find_element_by_id('webdata_now_p')
print(e.text) 

