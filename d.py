from time import sleep
from os import system
from sms import SendSms
import threading

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

            
while 1:
    system("cls||clear")
    print("""\033[38;2;255;0;0m

       R̴̢̪̜̝͙̯̩̙̓̊̊͒À̸̛̫N̶̢͚̣̲̝̠̰̣͚̈͋̓̽̓̚͝D̸̞͍̝̄̐̏̏O̵̡̻̟̜̮̱̤̫͎͗̓̑̿͂̇͝͝M̶̢͎̭͚̪͖̳̣̆̽͆G̶̪̜̮̰̫̳̎̓̍̈́̕͝͝Ŭ̶̹̝̦̭̤͋̆̈́͊̍̀̽Ý̸̪̭̗͌̒́̒͐́̅̐͝!̴̟̮͇̜͉̩͇̗̈́̈́͑
    
                                                  
                  :D                         
    
    \033[38;2;180;0;255mSms: {}\033[0m           \033[38;2;255;80;120m randomguy\by \n  
    """.format(len(servisler_sms)))
    try:
        menu = input("\033[38;2;180;0;255m 1- Normal\n\n 2- Hızlı (TURBO)\n\n 3- Çıkış\n\n\033[38;2;180;0;255m Seçim: \033[0m")
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print("\033[38;2;180;0;255mHatalı giriş yaptın. Tekrar deneyiniz.\033[0m")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        print("\033[38;2;180;0;255mTelefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): \033[38;2;180;0;255m", end="")
        tel_no = input("\033[0m")
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print("\033[38;2;180;0;255mTelefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: \033[38;2;180;0;255m", end="")
            dizin = input("\033[0m")
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print("\033[38;2;180;0;255mHatalı dosya dizini. Tekrar deneyiniz.\033[0m")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print("\033[38;2;180;0;255mHatalı telefon numarası. Tekrar deneyiniz.\033[0m") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print("\033[38;2;180;0;255mMail adresi (Bilmiyorsanız 'enter' tuşuna basın): \033[38;2;180;0;255m", end="")
            mail = input("\033[0m")
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print("\033[38;2;180;0;255mHatalı mail adresi. Tekrar deneyiniz.\033[0m") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print("\033[38;2;180;0;255mKaç adet SMS göndermek istiyorsun {}: \033[38;2;180;0;255m".format(sonsuz), end="")
            kere = input("\033[0m")
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print("\033[38;2;180;0;255mHatalı giriş yaptın. Tekrar deneyiniz.\033[0m") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print("\033[38;2;180;0;255mKaç saniye aralıkla göndermek istiyorsun: \033[38;2;180;0;255m", end="")
            aralik = int(input("\033[0m"))
        except ValueError:
            system("cls||clear")
            print("\033[38;2;180;0;255mHatalı giriş yaptın. Tekrar deneyiniz.\033[0m") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print("\033[38;2;180;0;255m\nMenüye dönmek için 'enter' tuşuna basınız..\033[0m")
        input()
    elif menu == 3:
        system("cls||clear")
        print("\033[38;2;180;0;255mÇıkış yapılıyor...\033[0m")
        break
    elif menu == 2:
        system("cls||clear")
        print("\033[38;2;180;0;255mTelefon numarasını başında '+90' olmadan yazınız: \033[38;2;180;0;255m", end="")
        tel_no = input("\033[0m")
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print("\033[38;2;180;0;255mHatalı telefon numarası. Tekrar deneyiniz.\033[0m") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print("\033[38;2;180;0;255mMail adresi (Bilmiyorsanız 'enter' tuşuna basın): \033[38;2;180;0;255m", end="")
            mail = input("\033[0m")
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print("\033[38;2;180;0;255mHatalı mail adresi. Tekrar deneyiniz.\033[0m") 
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()
        def Turbo():
            while not dur.is_set():
                thread = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    thread.append(t)
                    t.start()
                for t in thread:
                    t.join()
        try:
            Turbo()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)