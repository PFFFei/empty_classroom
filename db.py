#coding:utf-8
import os
import django
from bs4 import BeautifulSoup
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "empty_classroom.settings")
django.setup()

def Monday():
    global tr_list
    from tool.models import Monday

    for i in range(2,158):
        td_list = list(tr_list[i].find_all('td'))#57
        td_list_data = []
        for j in range(1,9):
            data = ''
            for line in td_list[j].stripped_strings:#去空输出标签下所有文本
                data += line + ' '
            td_list_data.append(data)   
        Monday.objects.create(classroom = td_list[0].text,
                              lesson_0102 = td_list_data[0],
                              lesson_0304 = td_list_data[1],
                              lesson_05 = td_list_data[2],
                              lesson_0607 = td_list_data[3],
                              lesson_0809 = td_list_data[4],
                              lesson_10 = td_list_data[5],
                              lesson_1112 = td_list_data[6],
                              lesson_13 = td_list_data[7])

def Tuesday():
    global tr_list
    from tool.models import Tuesday

    for i in range(2,158):
        td_list = list(tr_list[i].find_all('td'))
        td_list_data = []
        for j in range(9,17):
            data = ''
            for line in td_list[j].stripped_strings:
                data += line + ' '
            td_list_data.append(data)  
        Tuesday.objects.create(classroom = td_list[0].text,
                              lesson_0102 = td_list_data[0],
                              lesson_0304 = td_list_data[1],
                              lesson_05 = td_list_data[2],
                              lesson_0607 = td_list_data[3],
                              lesson_0809 = td_list_data[4],
                              lesson_10 = td_list_data[5],
                              lesson_1112 = td_list_data[6],
                              lesson_13 = td_list_data[7])

def Wednesday():
    global tr_list
    from tool.models import Wednesday

    for i in range(2,158):
        td_list = list(tr_list[i].find_all('td'))
        td_list_data = []
        for j in range(17,25):
            data = ''
            for line in td_list[j].stripped_strings:
                data += line + ' '
            td_list_data.append(data)    
        Wednesday.objects.create(classroom = td_list[0].text,
                              lesson_0102 = td_list_data[0],
                              lesson_0304 = td_list_data[1],
                              lesson_05 = td_list_data[2],
                              lesson_0607 = td_list_data[3],
                              lesson_0809 = td_list_data[4],
                              lesson_10 = td_list_data[5],
                              lesson_1112 = td_list_data[6],
                              lesson_13 = td_list_data[7])

def Thursday():
    global tr_list
    from tool.models import Thursday

    for i in range(2,158):
        td_list = list(tr_list[i].find_all('td'))
        td_list_data = []
        for j in range(25,33):
            data = ''
            for line in td_list[j].stripped_strings:
                data += line + ' '
            td_list_data.append(data)   
        Thursday.objects.create(classroom = td_list[0].text,
                              lesson_0102 = td_list_data[0],
                              lesson_0304 = td_list_data[1],
                              lesson_05 = td_list_data[2],
                              lesson_0607 = td_list_data[3],
                              lesson_0809 = td_list_data[4],
                              lesson_10 = td_list_data[5],
                              lesson_1112 = td_list_data[6],
                              lesson_13 = td_list_data[7])

def Friday():
    global tr_list
    from tool.models import Friday

    for i in range(2,158):
        td_list = list(tr_list[i].find_all('td'))
        td_list_data = []
        for j in range(33,41):
            data = ''
            for line in td_list[j].stripped_strings:
                data += line + ' '
            td_list_data.append(data)   
        Friday.objects.create(classroom = td_list[0].text,
                              lesson_0102 = td_list_data[0],
                              lesson_0304 = td_list_data[1],
                              lesson_05 = td_list_data[2],
                              lesson_0607 = td_list_data[3],
                              lesson_0809 = td_list_data[4],
                              lesson_10 = td_list_data[5],
                              lesson_1112 = td_list_data[6],
                              lesson_13 = td_list_data[7])

def Saturday():
    global tr_list
    from tool.models import Saturday

    for i in range(2,158):
        td_list = list(tr_list[i].find_all('td'))
        td_list_data = []
        for j in range(41,49):
            data = ''
            for line in td_list[j].stripped_strings:
                data += line + ' '
            td_list_data.append(data)   
        Saturday.objects.create(classroom = td_list[0].text,
                              lesson_0102 = td_list_data[0],
                              lesson_0304 = td_list_data[1],
                              lesson_05 = td_list_data[2],
                              lesson_0607 = td_list_data[3],
                              lesson_0809 = td_list_data[4],
                              lesson_10 = td_list_data[5],
                              lesson_1112 = td_list_data[6],
                              lesson_13 = td_list_data[7])

def Sunday():
    global tr_list
    from tool.models import Sunday

    for i in range(2,158):
        td_list = list(tr_list[i].find_all('td'))
        td_list_data = []
        for j in range(49,57):
            data = ''
            for line in td_list[j].stripped_strings:
                data += line + ' '
            td_list_data.append(data)   
        Sunday.objects.create(classroom = td_list[0].text,
                              lesson_0102 = td_list_data[0],
                              lesson_0304 = td_list_data[1],
                              lesson_05 = td_list_data[2],
                              lesson_0607 = td_list_data[3],
                              lesson_0809 = td_list_data[4],
                              lesson_10 = td_list_data[5],
                              lesson_1112 = td_list_data[6],
                              lesson_13 = td_list_data[7])


if __name__ == "__main__":

    path ='.\\classroom.html'
    
    htmlfile = open(path,'r')
    htmlhandle = htmlfile.read()

    soup = BeautifulSoup(htmlhandle,'lxml')

    tr_list = list(soup.find_all('tr'))
    Monday()
    print("Monday Done!")
    Tuesday()
    print("Tuesday Done!")
    Wednesday()
    print("Wednesday Done!")
    Thursday()
    print("Thursday Done!")
    Friday()
    print("Friday Done!")
    Saturday()
    print("Saturday Done!")
    Sunday()
    print("Sunday Done!")
    print("All Done!")
