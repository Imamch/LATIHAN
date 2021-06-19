# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 23:21:14 2021

@author: imamc
"""

#Pengulangan
jwb = "y"
while jwb=="y" or jwb=="Y":
    print('===============')
    print('Transaksi Pembelian printer diskon 15% jika nominal pembelian >1,5jt')
    print('===============')
    
    #Nilai awal variable jblbeli = harga 1 printer
    harga1print = 660000

    #Input Jumblah beli
    jblbeli= input ('Masukkan jumblah printer Epson T20 yang dibeli = ')

    #Perhitungan total harga pembelian
    #Total harga= int(harga1print) * int(jblbeli)
    if int((harga1print)*int(jblbeli))>1500000:
        diskon=int(((harga1print)*int(jblbeli))*0.15)
        totalharga=int(((harga1print)*int(jblbeli))-int(diskon))
        print(totalharga)  
    else:
       sts=int((harga1print)*int(jblbeli))
       print(sts)
       
    #Input Break
    jwb = input(">>> Apakah Anda ingin input lagi ? y/t : ")
    if jwb== "t" or jwb=="T":
        break

  