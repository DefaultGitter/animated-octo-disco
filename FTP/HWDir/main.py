# Ви працюєте у компанії, яка зберігає важливі файли на локальному сервері.
# Для забезпечення безпеки даних необхідно щодня створювати резервні копії цих файлів
# та надсилати їх на FTP-сервер для зберігання у хмарному сховищі.
# Вимоги:
# Напишіть скрипт на Python, який автоматично створюватиме резервні копії заданих файлів.
# Скрипт повинен підключатися до FTP-сервера та завантажувати створені резервні копії на сервер.
# Налаштуйте скрипт так, щоб він виконувався щодня у певний час.
# Забезпечте логування дій скрипта, щоб можна було відстежувати його роботу.

import ftplib
import logging
from datetime import datetime

c_time = f'{datetime.now():%d-%m-%Y}'

logging.basicConfig(level=logging.INFO, filename=f'{c_time}.log', filemode='w',
                    format='%(asctime)s %(levelname)s - %(message)s')

try:
    with ftplib.FTP('127.0.0.1') as ftp:
        ftp.login(user='test', passwd='123456')

        with open('from_user.txt', 'rb') as file:
            ftp.storbinary('STOR ' + 'from_user.txt', file)
    logging.info('data copied successfully')
except ConnectionRefusedError:
    logging.critical('can not connect to server')
except ftplib.error_perm:
    logging.error('incorrect username or password')
except FileNotFoundError:
    logging.error('can not find file or directory')
