#coding:utf-8
#还未运行
import os
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "empty_classroom.settings")
django.setup()

def Monday_change():
	from tool.models import Monday

	info = Monday.objects.all()
	global week_info,week_change

	for each in info:
		for i in range(len(week_change)):
			if re.findall(r'[(](.*?)[)]', each.lesson_0102) == week_info[i]:
				Monday.objects.filter(classroom = each).update(lesson_0102 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0304) == week_info[i]:
				Monday.objects.filter(classroom = each).update(lesson_0304 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_05) == week_info[i]:
				Monday.objects.filter(classroom = each).update(lesson_05 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0607) == week_info[i]:
				Monday.objects.filter(classroom = each).update(lesson_0607 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0809) == week_info[i]:
				Monday.objects.filter(classroom = each).update(lesson_0809 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_10) == week_info[i]:
				Monday.objects.filter(classroom = each).update(lesson_10 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_1112) == week_info[i]:
				Monday.objects.filter(classroom = each).update(lesson_1112 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_13) == week_info[i]:
				Monday.objects.filter(classroom = each).update(lesson_13 = week_change[i])

def Tuesday_change():
	from tool.models import Tuesday

	info = Tuesday.objects.all()
	global week_info,week_change

	for each in info:
		for i in range(len(week_change)):
			if re.findall(r'[(](.*?)[)]', each.lesson_0102) == week_info[i]:
				Tuesday.objects.filter(classroom = each).update(lesson_0102 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0304) == week_info[i]:
				Tuesday.objects.filter(classroom = each).update(lesson_0304 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_05) == week_info[i]:
				Tuesday.objects.filter(classroom = each).update(lesson_05 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0607) == week_info[i]:
				Tuesday.objects.filter(classroom = each).update(lesson_0607 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0809) == week_info[i]:
				Tuesday.objects.filter(classroom = each).update(lesson_0809 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_10) == week_info[i]:
				Tuesday.objects.filter(classroom = each).update(lesson_10 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_1112) == week_info[i]:
				Tuesday.objects.filter(classroom = each).update(lesson_1112 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_13) == week_info[i]:
				Tuesday.objects.filter(classroom = each).update(lesson_13 = week_change[i])

def Wednesday_change():
	from tool.models import Wednesday

	info = Wednesday.objects.all()
	global week_info,week_change

	for each in info:
		for i in range(len(week_change)):
			if re.findall(r'[(](.*?)[)]', each.lesson_0102) == week_info[i]:
				Wednesday.objects.filter(classroom = each).update(lesson_0102 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0304) == week_info[i]:
				Wednesday.objects.filter(classroom = each).update(lesson_0304 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_05) == week_info[i]:
				Wednesday.objects.filter(classroom = each).update(lesson_05 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0607) == week_info[i]:
				Wednesday.objects.filter(classroom = each).update(lesson_0607 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0809) == week_info[i]:
				Wednesday.objects.filter(classroom = each).update(lesson_0809 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_10) == week_info[i]:
				Wednesday.objects.filter(classroom = each).update(lesson_10 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_1112) == week_info[i]:
				Wednesday.objects.filter(classroom = each).update(lesson_1112 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_13) == week_info[i]:
				Wednesday.objects.filter(classroom = each).update(lesson_13 = week_change[i])

def Thursday_change():
	from tool.models import Thursday

	info = Thursday.objects.all()
	global week_info,week_change

	for each in info:
		for i in range(len(week_change)):
			if re.findall(r'[(](.*?)[)]', each.lesson_0102) == week_info[i]:
				Thursday.objects.filter(classroom = each).update(lesson_0102 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0304) == week_info[i]:
				Thursday.objects.filter(classroom = each).update(lesson_0304 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_05) == week_info[i]:
				Thursday.objects.filter(classroom = each).update(lesson_05 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0607) == week_info[i]:
				Thursday.objects.filter(classroom = each).update(lesson_0607 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0809) == week_info[i]:
				Thursday.objects.filter(classroom = each).update(lesson_0809 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_10) == week_info[i]:
				Thursday.objects.filter(classroom = each).update(lesson_10 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_1112) == week_info[i]:
				Thursday.objects.filter(classroom = each).update(lesson_1112 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_13) == week_info[i]:
				Thursday.objects.filter(classroom = each).update(lesson_13 = week_change[i])

def Friday_change():
	from tool.models import Friday

	info = Friday.objects.all()
	global week_info,week_change

	for each in info:
		for i in range(len(week_change)):
			if re.findall(r'[(](.*?)[)]', each.lesson_0102) == week_info[i]:
				Friday.objects.filter(classroom = each).update(lesson_0102 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0304) == week_info[i]:
				Friday.objects.filter(classroom = each).update(lesson_0304 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_05) == week_info[i]:
				Friday.objects.filter(classroom = each).update(lesson_05 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0607) == week_info[i]:
				Friday.objects.filter(classroom = each).update(lesson_0607 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0809) == week_info[i]:
				Friday.objects.filter(classroom = each).update(lesson_0809 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_10) == week_info[i]:
				Friday.objects.filter(classroom = each).update(lesson_10 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_1112) == week_info[i]:
				Friday.objects.filter(classroom = each).update(lesson_1112 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_13) == week_info[i]:
				Friday.objects.filter(classroom = each).update(lesson_13 = week_change[i])

def Saturday_change():
	from tool.models import Saturday

	info = Saturday.objects.all()
	global week_info,week_change

	for each in info:
		for i in range(len(week_change)):
			if re.findall(r'[(](.*?)[)]', each.lesson_0102) == week_info[i]:
				Saturday.objects.filter(classroom = each).update(lesson_0102 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0304) == week_info[i]:
				Saturday.objects.filter(classroom = each).update(lesson_0304 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_05) == week_info[i]:
				Saturday.objects.filter(classroom = each).update(lesson_05 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0607) == week_info[i]:
				Saturday.objects.filter(classroom = each).update(lesson_0607 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0809) == week_info[i]:
				Saturday.objects.filter(classroom = each).update(lesson_0809 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_10) == week_info[i]:
				Saturday.objects.filter(classroom = each).update(lesson_10 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_1112) == week_info[i]:
				Saturday.objects.filter(classroom = each).update(lesson_1112 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_13) == week_info[i]:
				Saturday.objects.filter(classroom = each).update(lesson_13 = week_change[i])

def Sunday_change():
	from tool.models import Sunday

	info = Sunday.objects.all()
	global week_info,week_change

	for each in info:
		for i in range(len(week_change)):
			if re.findall(r'[(](.*?)[)]', each.lesson_0102) == week_info[i]:
				Sunday.objects.filter(classroom = each).update(lesson_0102 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0304) == week_info[i]:
				Sunday.objects.filter(classroom = each).update(lesson_0304 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_05) == week_info[i]:
				Sunday.objects.filter(classroom = each).update(lesson_05 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0607) == week_info[i]:
				Sunday.objects.filter(classroom = each).update(lesson_0607 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_0809) == week_info[i]:
				Sunday.objects.filter(classroom = each).update(lesson_0809 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_10) == week_info[i]:
				Sunday.objects.filter(classroom = each).update(lesson_10 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_1112) == week_info[i]:
				Sunday.objects.filter(classroom = each).update(lesson_1112 = week_change[i])
			if re.findall(r'[(](.*?)[)]', each.lesson_13) == week_info[i]:
				Sunday.objects.filter(classroom = each).update(lesson_13 = week_change[i])


if __name__ == "__main__":
	week_change = ['1,2,4,5', '1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '5,15', '15', '1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '4,5', '1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '5,6', '4,8', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '10,11,12,13,14,15,16,17', '5,6,3', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16', '4,8,6,7', '6,7', '1,2,3,4,5,6,8,9,15', '15,5', '2,4', '5', '2,3,8,9,4,5', '8,9,4,5,2,3,6', '2,3,6,4,5', '4,5,2,3,6,7', '4,5,1,2', '4,5', '4', '2,3,4,5,6,7,8,9,10,11,12,13,14', '3,4', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '4,5,6,7,8,9,10,11', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,5,6,7,8,12,13,14,15', '1,2,3,4,5,6,7,8,12,13,14,15,16,17', '1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17', '1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,3,5,7,9,11,13,15,17', '1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17','1,2,3,4,5,6,7,8,11,12,13,14', '1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17','1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17', '4,9,12,15,5,10,13,16', '4,9,12,15,6,11,14,17,5,10,13,16', '4,9,12,15', '1,2,3,4,5,6,7,8,14,15,16,17', '4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,5,7,8,9', '1,2,4,5,6,7,8,9,13,14,15,16', '1,2,4,5,6,7,8,9', '4,5,6,7,8,9,10,11,14,15,16,17', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '5,6,7,8,16,17', '4,5,6,7,8,9,10,11,13,14,15,16', '1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17','4,5,6,7,8,9,10,11,14,15,16,17', '1,2,4,5,6,7,8,9,16,17', '1,2,3,4,5,6,7,8', '1,2,3,4,5,6,7,8,9,10,11,12', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,3,5,7,9,11,13,15,17','1,2,3,4,5,6,7,8,9,10,11,12', '1,2,3,4,5,6,7,8,9,10,11,12', '1,2,3,4,5,6,8,9', '1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17', '14,15,16,17', '1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17', '1', '4,5,6,7,8,9,10,11,12,13,14,15,16,17', '4,5,6,7,8,9,10,11', '6,8,9,10,11,12,13,14,15', '4,9,12,15', '4,5,6,7,9,10,11,12', '1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,4,5,6,8,9,10,11', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,5,6,7,8,16,17', '4,1,3,5,7,9,11,13,15,17', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17', '1,2,3,4,5,6,7,8,11,12,13,14,15,16,17', '1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '2,4,6,8,10,12,14,16', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,5,6,7,8,10,11,13,14,16,17', '6,7,16', '9,10,3,5,6,7,8', '2,3,10,13,7,6,5,8', '6,7,8,9,10,11', '1,2,10,11,14,15', '2,3,9,10,8,4,5,6', '12,13', '3,6,2,7', '2,3,13,14', '16', '3,9,10,5,6,7,8', '10,4,13,7,6,5,8,2,3', '6,7,8,9,10,11', '2,3,8,4,5,6,9,10', '6', '8']
	week_info = [['1-2周', '4-5周'], ['1-2周', '4-17周'], ['5周', '15周'], ['15周'], ['1,3-17周'], ['4-5周'], ['4-17周', '1-2周'], ['5-6周'], ['4,8周'], ['听说技能训练', '1-17单周', '4,6,8,10,12,14,16周'], ['10-17周'], ['5周', '6周', '3周'], ['1-8周', '9-16周'], ['4,8周', '6-7周'], ['6-7周'], ['6周', '8-9周', '3-4周', '1-2周', '15周', '5周'], ['15周', '5周'], ['2周', '4周'], ['5周'], ['2-3周', '8-9周', '4-5周'], ['8-9周', '4-5周', '2周', '3周', '6周'], ['2周', '3周', '6周', '4-5周'], ['4-5周', '2-3周', '6-7周'], ['4-5周', '1-2周'], ['5周', '4周'], ['4周'], ['2-14周'], ['3-4周'], ['1-9周', '10-17周'], ['4-11周'], ['1-17单周', '2,4,6,8,10,12,14,16周'], ['1-8周', '12-15周'], ['1-8周', '16-17周', '12-15周'], ['1-7,9-17周'], ['4,6,8,10,12,14,16周', '听说技能训练', '1,3,5,7,9,11,13,15,17周'], ['4,6,8,10,12,14,16周', '1,3,5,7,9,11,13,15,17周'], ['听说技能训练', '1,3,5,7,9,11,13,15,17周'], ['1-8周', '10-17周'], ['1-8,11-14周'], ['1-8周', '9,11-17周'], ['9,11-17周', '1-8周'], ['4,9,12,15周', '5,10,13,16周'], ['4,9,12,15周', '6,11,14,17周', '5,10,13,16周'], ['4,9,12,15周'], ['1-4周', '14-17周', '5-8周'], ['16-17周', '4-7周', '8-11周', '12-15周'], ['1-5,7-9周'], ['13-16周', '外', '1-2,4-9周'], ['外', '1-2,4-9周'], ['14-17周', '4-7周', '8-11周'], ['1-12周', '13-17周'], ['5-8周', '16-17周'], ['4-7周', '8-11周', '13-16周'], ['14-17周', '5-8周', '9-12周', '1-4周'], ['8-11周', '14-17周', '4-7周'], ['1-2,4-9周', '16-17周'], ['外', '1-8周'], ['1-8周', '9-12周'], ['1,3,5,7,9,11,13,15,17周', '2,4,6,8,10,12,14,16周'], ['外', '1-17周'], ['1-17单周'], ['1-12周'], ['Financial Management', '1-12周'], ['外', '1-6,8-9周'], ['1-5,7-17周'], ['14-17周'], ['ACCA', '1-10,12-17周'], ['1周'], ['4-5周', '16-17周'], ['4-7周', '8-11周'], ['6周', '12-15周', '8-11周'], ['实验', '4,9,12,15周'], ['9-12周', '4-7周'], ['听说技能训练', '1,3,5,7,9,11,13,15,17单周', '4,6,8,10,12,14,16周'], ['1,4-6,8-11周'], ['1-17周', '2,4,6,8,10,12,14,16周'], ['1-8周', '16-17周'], ['4周', '1,3,5,7,9,11,13,15,17周'], ['ERP', '1-17周'], ['10-17周', '1-8周'], ['11-17周', '1-8周'], ['1,3,5,7,9,11,13,15,17周', '4,6,8,10,12,14,16周'], ['2,4,6,8,10,12,14,16周', '1-17单周'], ['2,4,6,8,10,12,14,16周', '2,4,6,8,10,12,14,16周'], ['3-17周', '1-17周'], ['4周', '1-3,5-8,10-11,13-14,16-17周'], ['6-7周', '16周'], ['9-10周', '3周', '5周', '6周', '7周', '8周'], ['2-3周', '10周', '13周', '7周', '6周', '5周', '8周'], ['6-7周', '8-9周', '10-11周'], ['1-2周', '10-11周', '8-9周', '14-15周'], ['2-3周', '9-10周', '8周', '4周', '5周', '6周'], ['12-13周'], ['3周', '6周', '2周', '7周'], ['2-3周', '13-14周'], ['16周'], ['3周', '9-10周', '5周', '6周', '7周', '8周'], ['10周', '4周', '13周', '7周', '6周', '5周', '8周', '2-3周'], ['6-7周', '10-11周', '8-9周'], ['2-3周', '8周', '4周', '5周', '6周', '9-10周'], ['6周'], ['8周']]
	Monday_change()
	print("Monday_change done!")
	Tuesday_change()
	print("Tuesday_change done!")
	Wednesday_change()
	print("Wednesday_change done!")
	Thursday_change()
	print("Thursday_change done!")
	Friday_change()
	print("Friday_change done!")
	Saturday_change()
	print("Saturday_change done!")
	Sunday_change()
	print("Sunday_change done!")
	# print(week_info)
	# print(len(week_info))

