# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 09:55:42 2021

@author: imamc
"""

#cek kelulusan, jika nilai >60 maka status lulus
print ("===================")
print (" cek kelulusan ")
print ("===================")
#setiap value yang diimputkan, secara default bertipe data string
n = input(">> masukkan nilai = ")
#cek nilai
if int(n)>60:
    sts='LULUS'
else: 
    sts='ULANG'
    
print (sts)


