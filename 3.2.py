def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    if "@" not in recipient and sender :
        print("Невозможно отправить письмо с адреса", sender," на адрес ", recipient)
    else:
        if  (".com" or ".ru" or ".net") not in recipient and sender:
            print("Невозможно отправить письмо с адреса", sender, " на адрес ", recipient)
        else:
            if recipient == sender:
                print( "Нельзя отправить письмо самому себе!")
            else:
                if sender == 'university.help@gmail.com':
                    print ("Письмо успешно отправлено с адреса ",sender," на адрес ",recipient, ".")
                else: print( "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.ru')
