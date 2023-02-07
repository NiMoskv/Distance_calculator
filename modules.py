import datetime as dt



def get_days_to_birthday(name, date_birthday):
    date_birthday=dt.datetime.strptime(date_birthday,"%d,%m,%Y")
    date_birthday=date_birthday.date()
    today=dt.date.today()
    date_birthday=date_birthday.replace(year=today.year)
    if today>date_birthday:
        date_birthday=date_birthday.replace(year=today.year+1)
    return f'{name}, до твоего дня рождения осталось дней : {date_birthday-today}'


entry_massiv=[('Nikita',"8,3,1996"),('Alexandra',"4,11,2002"),('Vasiyok',"28,9,1996")]

for i in entry_massiv:
    print(get_days_to_birthday(i[0],i[1]))