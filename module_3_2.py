def send_email(message, recipient, *, sender="university.help@gmail.com"):
    flag = False
    sim = '@'
    com = '.com'
    ru = '.ru'
    net = '.net'

    if sim in recipient and sim in sender:
        if ((com in recipient or ru in recipient or net in recipient)
                and (com in sender or ru in sender or net in sender)):
            flag = True
    if flag is False:
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
        return False
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return False
    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.')
        return True
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.')
        return True

send_email('Проверка сообщения', 'fanfik@mail.ru')
send_email('Проверка на нестандартного отправителя',
           'google@gmail.com', sender='university.str@gmail.com')
send_email('Проверка на окончание email', 'rustam@mail.n')
send_email('Проверка на отправку письма самомму себе', 'good@yandex.ru', sender='good@yandex.ru')