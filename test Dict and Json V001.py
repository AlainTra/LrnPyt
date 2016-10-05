# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:15:45 2016

@author: Alain GMG
"""
import json

print(" - Build dict")

dicRes = {}  
dicRes['res'] = []  

for i in range(5000):
    dicRes['res'].append({  
        'id' : 100+i ,
        'num' : [ 10+i, 20+i, 30+i, 40+i, 50+i ] ,
        'str' : [6+i, 7+i ] ,
        'dat' : '15-Jun-2016' ,
        'win': True
    })

print(" - Export dict to Json")

#with open('data.json', 'w') as outfile:  
#    json.dump(data, outfile)
    
with open('data_formated.json', 'w') as outfile:  
    json.dump(dicRes, outfile, indent=1)

   
print("* DONE *")
   