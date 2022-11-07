from datetime import datetime, timedelta

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
#--------------------Визначаємо потрібний проміжок днів тижня (робочі - вихідні)---------------------
def find_interval():
    if datetime.now().weekday() == 5:           # Якщо сьогодні субота
        interval = timedelta(days=6)       
    elif datetime.now().weekday() == 6:         # Якщо сьогодні неділя
        interval = timedelta(days=5)
    else:                                       # Якщо сьогодні будь-який робочий день
        interval = timedelta(days=7)
    return interval

#----------------Функція відбору іменинників на наступний тиждень-----------------
def get_birthdays_per_week(users):
    
    celebrating_birthbays = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }

    interval = find_interval()
    future_daytime = datetime.now() + interval
 #---------------Перебір персон в заданому списку-----------------    
    for person in users:
        this_year_birthday = datetime(year=datetime.now().year, month=person.get("birthday").month, day=person.get("birthday").day)
#--------------Вибір дати в проміжку від поточної дати і на визначений інтервал вперед--------------       
        if datetime.now() <= this_year_birthday <= future_daytime:
            weekday_string = this_year_birthday.strftime("%A")
            if weekday_string in ["Saturday", "Sunday"]:
                weekday_string = "Monday"
            celebrating_birthbays.get(weekday_string).append(person.get("name"))
    print_birthday_people(celebrating_birthbays)

#----------------Функція виводу на екран списку іменинників------------------
def print_birthday_people(celebrating_birthbays: dict):
    for key, value in celebrating_birthbays.items():
        if value:
            print(f"{key}: {', '.join(value)}")

#----------------Точка входу---------------------------------
if __name__ == "__main__":
    get_birthdays_per_week(users_birthday)
