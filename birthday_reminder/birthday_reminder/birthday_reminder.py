from datetime import datetime
#-----------Список знайомих із днями народження--------------------
users_birthday = [
    {"name": "Maks Kuznetsov", "birthday": datetime(year=1986, month=11, day=5)},
    {"name": "Ihor Bikovskii", "birthday": datetime(year=1978, month=11, day=6)},
    {"name": "Anna Berezkina", "birthday": datetime(year=1985, month=11, day=6)},
    {"name": "Anatolii Karteleev", "birthday": datetime(year=1984, month=11, day=6)},
    {"name": "Olena Korotchuk", "birthday": datetime(year=1975, month=11, day=7)},
    {"name": "Anastasiia Olshanovska", "birthday": datetime(year=1980, month=11, day=10)},
    {"name": "Ihor Holovatyi", "birthday": datetime(year=1989, month=11, day=12)},
    {"name": "Oleksandr Pidoprygora", "birthday": datetime(year=1986, month=11, day=13)},
    {"name": "Andrii Kutnii", "birthday": datetime(year=1986, month=11, day=15)},
    {"name": "Oleksandra Abdurashitova", "birthday": datetime(year=1990, month=11, day=17)},
    {"name": "Natalia Masik", "birthday": datetime(year=1987, month=11, day=17)},
    {"name": "Ihor Chepilenko", "birthday": datetime(year=1987, month=11, day=18)},
    {"name": "Stanislav Kulik", "birthday": datetime(year=1980, month=11, day=18)},
    {"name": "Mykhailo Jadan", "birthday": datetime(year=1984, month=11, day=21)},
    {"name": "Oleksii Metelkin", "birthday": datetime(year=1985, month=11, day=22)},
    {"name": "Alyona Bazylevich", "birthday": datetime(year=1985, month=11, day=24)},
    {"name": "Illya Padalkin", "birthday": datetime(year=1987, month=11, day=25)},
    {"name": "Roman Chaplynskyi", "birthday": datetime(year=1988, month=11, day=26)},
    {"name": "Viktoria Stankevich", "birthday": datetime(year=1985, month=11, day=27)},
    {"name": "Mykhailo Natalchenko", "birthday": datetime(year=1985, month=11, day=29)},
    {"name": "Anna Lapinska", "birthday": datetime(year=1990, month=11, day=29)}
]

def get_birthdays_per_week(users):
   
    mon = []
    tue = []
    wed = []
    thur = []
    fri = []
#--------------Дата, період якої враховується при формуванні результату (7 днів)--------------------
    future_daytime = datetime(datetime.now().date().year, datetime.now().date().month, ((datetime.now().date().day) + 7)).date()
#--------------Перебір персон в заданому списку-----------------    
    for dict_1 in users:
        birth_date = dict_1["birthday"]                                            #---з цієї змінної не виділяються дні/місяці
        birth_date_str = datetime.strftime(birth_date, '%Y-%m-%d')                 
        result_birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
#--------------Цьогорішня дата дня народження-----------------------       
        this_year_birthday = datetime(datetime.now().date().year, result_birth_date.month, result_birth_date.day).date()    
#--------------Вибір дати в проміжку від поточної дати і на 7 днів вперед--------------        
        if datetime.now().date() <= this_year_birthday <= future_daytime: 
            if this_year_birthday.weekday() == 1:
                tue.append(dict_1["name"])
            elif this_year_birthday.weekday() == 2:
                wed.append(dict_1["name"])
            elif this_year_birthday.weekday() == 3:
                thur.append(dict_1["name"])
            elif this_year_birthday.weekday() == 4:
                fri.append(dict_1["name"])
            else:
                mon.append(dict_1["name"])
        else:
            continue

    mon_string = ", ".join(mon)
    tue_string = ", ".join(tue)
    wed_string = ", ".join(wed)
    thur_string = ", ".join(thur)
    fri_string = ", ".join(fri)
#-------------Вивід по дням тижня іменинників наступного тижня---------------    
    if len(mon) > 0:
        print(f"Monday: {mon_string}")
    if len(tue) > 0:
        print(f"Tuesday: {tue_string}")
    if len(wed) > 0:
        print(f"Wednesday: {wed_string}")
    if len(thur) > 0:
        print(f"Thursday: {thur_string}")
    if len(fri) > 0:
        print(f"Friday: {fri_string}")
#------------Фінальний аккорд---------------------
    return print("Don`t forget to say HAPPY BIRTHDAY to them!!!")

if __name__ == '__main__':
    get_birthdays_per_week(users_birthday)
