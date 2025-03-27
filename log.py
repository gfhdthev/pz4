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
    def wrapper():
        func()
        func_name = func.__name__
        #создаем таблицу
        if os.path.isfile('name.csv'):
            file_df = pd.read_csv('name.csv')
            data = {'': [len(file_df)], "Пользователь": [user], "Действие": [func_name],"Дата": [now_time()],"Время":[sec()]} #создаем столбцы
            df = pd.DataFrame(data) #создаем сам датафрейм
            #df.loc[len(df)] = [user,func_name,now_time(),sec()] #задаем значения, которые надо вывести в строку
            df.to_csv('name.csv', mode='a', index=False, header=False)
        else:
            data = {"Пользователь": [user], "Действие": [func_name],"Дата": [now_time()],"Время":[sec()]} #создаем столбцы
            df = pd.DataFrame(data) #создаем сам датафрейм
            #df.loc[len(df)] = [user,func_name,now_time(),sec()] #задаем значения, которые надо вывести в строку
            df.to_csv('name.csv')
        return df
    return wrapper

@logging
def hello():
    print('Hello')
hello()

@logging
def bye():
    print('bye')
bye()