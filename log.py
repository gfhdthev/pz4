#Gfhdthev
#Логирование


#импортируем библиотеки
import os
import datetime
import pandas as pd

#берем имя пользователя компьютера
user=os.getlogin()

#работа с временем
def now_time():
    now_date=datetime.datetime.now().strftime('%d.%m.%Y') #полное время, включая год, месяц и т.д.
    return now_date
def sec():
    now_datetime=str(datetime.datetime.now()).split() #разделяем на дату и время
    current_time= now_datetime[1] #берем только время
    return current_time


def logging(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        func_name = func.__name__#берем имя функции
        #создаем таблицу
        if os.path.isfile('name.csv'):#проверяем, существует ли файл
            file_df = pd.read_csv('name.csv')
            data = {'': [len(file_df)], "Пользователь": [user], "Действие": [func_name],"Дата": [now_time()],"Время":[sec()]} #создаем столбцы
            df = pd.DataFrame(data) #создаем сам датафрейм
            df.to_csv('name.csv', mode='a', index=False, header=False)
        else:
            data = {"Пользователь": [user], "Действие": [func_name],"Дата": [now_time()],"Время":[sec()]} #создаем столбцы
            df = pd.DataFrame(data) #создаем сам датафрейм
            df.to_csv('name.csv')
        return result
    return wrapper
