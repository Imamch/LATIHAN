# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:01:23 2021

@author: imamc
"""

print ('==================')
print ('GOLONGAN USIA')
print ('==================')

u=input('>>> Masukkan usia=')
#cek masukan batasan usia 0-100
if int(u)>0 and int(u)<100:
    if int(u)>=60: 
        sts='lansia'
    elif int(u)>=35: 
        sts='dewasa'
    elif int(u)>=18: 
        sts='Pemuda'
    elif int(u)>=15: 
        sts='remaja'
    else:
        sts='anak-anak'
    print(sts)
else:
    pesan='>>> Masukkan usian 1-99 saja'
    print(pesan)