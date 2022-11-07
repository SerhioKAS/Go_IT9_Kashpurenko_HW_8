from setuptools import setup, find_namespace_packages

setup(
    name='birthday_reminder',
    version='1.0.0',
    description='Script helps to remind your friends birthdays',
    url='http://github.com/SerhioKAS/Go_IT9_Kashpurenko_HW_8',
    author='Kashpurenko',
    author_email='sarhiokas@gmail.com',
    license='MIT',
    platforms='windows, unix',
    packages=find_namespace_packages(),
    entry_points={'console_scripts' : ['birthday-reminder = birthday_reminder.birthday_reminder: get_birthdays_per_week']}
)