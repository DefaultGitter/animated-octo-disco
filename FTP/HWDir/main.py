# Ви працюєте у компанії, яка зберігає важливі файли на локальному сервері.
# Для забезпечення безпеки даних необхідно щодня створювати резервні копії цих файлів
# та надсилати їх на FTP-сервер для зберігання у хмарному сховищі.

# Вимоги:
# Напишіть скрипт на Python, який автоматично створюватиме резервні копії заданих файлів.
# Скрипт повинен підключатися до FTP-сервера та завантажувати створені резервні копії на сервер.
# Налаштуйте скрипт так, щоб він виконувався щодня у певний час.
# Забезпечте логування дій скрипта, щоб можна було відстежувати його роботу.

from ftplib import FTP

with FTP('127.0.0.1') as ftp:
    ftp.login(user='test', passwd='123456')
    # ftp.dir()

    # ftp.retrlines('NLST')
    # for i in ftp.nlst():
    #     print(i)

    # ftp.cwd('folder_2')
    # ftp.retrlines('NLST')

    # ftp.mkd('new_folder')

    # ftp.rmd('new_folder')

    # ftp.rename('text.txt', 'book.txt')
    # ftp.rename('t_folder', 'folder_1')

    # ftp.delete('book.txt')

    # with open('from_user.txt', 'rb') as file:
    #     ftp.storbinary('STOR ' + 'from_user.txt', file)
    #     ftp.storbinary('STOR ' + file.name, file)

    with open('from_server.txt', 'wb') as file:
        ftp.retrbinary('RETR ' + 'from_server.txt', file.write)
