#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
from pyfiglet import Figlet

def main():
    figletFont = Figlet(font='slant')
    os.system("clear")
    print(figletFont.renderText("Arayüz ile Port Tara!"))

    loadingMessage = "Tüm fonksiyonları kullanabilmek için programı root yetkisi ile çalıştırın!"
    print(loadingMessage)
    print("[                    ] 0% ")
    time.sleep(1)
    print("[==========          ] 50%")
    time.sleep(1)
    print("[====================] 100%")
    time.sleep(3)

    os.system("clear")

    while True:
        print("""
        Yapmak İstediğiniz Fonksiyonu Seçin
        1-  Hızlı Tarama
        2-  Servis ve Versiyon Bilgisi
        3-  İşletim Sistemi Bilgisi
        4-  Sunucu/İstemci Keşfet
        5-  Dosya ile Tarama (-iL)
        6-  TCP/Syn Taraması
        7-  TCP/Connect Taraması
        8-  FIN Taraması
        9-  XMas Taraması
        10- Null Taraması
        11- UDP Taraması
        12- IP Protocol Taraması
        13- ACK Taraması
        14- ICMP Echo Request
        15- TCP ACK Ping
        16- UDP Ping
        """)

        transactionNumber = input("Yapmak İstediğiniz Fonksiyon Numarasını Girin (Programı sonlandırmak için 'q' girin): ")

        if transactionNumber == "q":
            print("Program Sonlandırılıyor...")
            break
        elif transactionNumber == "1":
            tValue = input("İşlem hızını girin (0-5 arası): ")
            targetIp = input("Hedef IP adresini girin: ")
            if tValue.isdigit() and 0 <= int(tValue) <= 5:
                os.system("nmap " + "-T "+ tValue +" "+ targetIp)
            else:
                print("Geçersiz işlem hızı. Lütfen 0 ile 5 arasında bir değer girin.")
        elif transactionNumber == "2":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -sS -sV " + targetIp)
        elif transactionNumber == "3":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -O " + targetIp)
        elif transactionNumber == "4":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -sP " + targetIp+"/24")
        elif transactionNumber == "5":
            print("Örnek: /home/usr/Dosyalar/liste")
            filePath = input("Dosya yolunu girin: ")
            os.system("nmap -iL " + filePath)
        elif transactionNumber == "6":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -sS -v " + targetIp)
        elif transactionNumber == "7":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -sT -v " + targetIp)
        elif transactionNumber == "8":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -sF -v " + targetIp)
        elif transactionNumber == "9":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -sX -v " + targetIp)
        elif transactionNumber == "10":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -sN -v " + targetIp)
        elif transactionNumber == "11":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -sU -v " + targetIp)
        elif transactionNumber == "12":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -sO -v " + targetIp)
        elif transactionNumber == "13":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -sA -v " + targetIp+" --reason")      
        elif transactionNumber == "14":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -PE " + targetIp)     
        elif transactionNumber == "15":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -PA " + targetIp)         
        elif transactionNumber == "16":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nmap -PU " + targetIp+ " -Pn")  
            
                           
                                                       
        else:
            print("Geçersiz giriş. Lütfen doğru bir fonksiyon numarası girin.")

if __name__ == "__main__":
    main()
