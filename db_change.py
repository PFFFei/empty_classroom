#coding:utf-8
#list index未报错 应该是Monday_change中的week_info问题
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
		week_0102 = re.findall(r'[(](.*?)[)]', each.lesson_0102)
		week_0304 = re.findall(r'[(](.*?)[)]', each.lesson_0304)
		week_05 = re.findall(r'[(](.*?)[)]', each.lesson_05)
		week_0607 = re.findall(r'[(](.*?)[)]', each.lesson_0607)
		week_0809 = re.findall(r'[(](.*?)[)]', each.lesson_0809)
		week_10 = re.findall(r'[(](.*?)[)]', each.lesson_10)
		week_1112 = re.findall(r'[(](.*?)[)]', each.lesson_1112)
		week_13 = re.findall(r'[(](.*?)[)]', each.lesson_13)
		if week_0102 not in week_info:
			week_info.append(week_0102)
		if week_0304 not in week_info:
			week_info.append(week_0304)
		if week_05 not in week_info:
			week_info.append(week_05)
		if week_0607 not in week_info:
			week_info.append(week_0607)
		if week_0809 not in week_info:
			week_info.append(week_0809)
		if week_10 not in week_info:
			week_info.append(week_10)
		if week_1112 not in week_info:
			week_info.append(week_1112)
		if week_13 not in week_info:
			week_info.append(week_13)

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
		week_0102 = re.findall(r'[(](.*?)[)]', each.lesson_0102)
		week_0304 = re.findall(r'[(](.*?)[)]', each.lesson_0304)
		week_05 = re.findall(r'[(](.*?)[)]', each.lesson_05)
		week_0607 = re.findall(r'[(](.*?)[)]', each.lesson_0607)
		week_0809 = re.findall(r'[(](.*?)[)]', each.lesson_0809)
		week_10 = re.findall(r'[(](.*?)[)]', each.lesson_10)
		week_1112 = re.findall(r'[(](.*?)[)]', each.lesson_1112)
		week_13 = re.findall(r'[(](.*?)[)]', each.lesson_13)
		if week_0102 not in week_info:
			week_info.append(week_0102)
		if week_0304 not in week_info:
			week_info.append(week_0304)
		if week_05 not in week_info:
			week_info.append(week_05)
		if week_0607 not in week_info:
			week_info.append(week_0607)
		if week_0809 not in week_info:
			week_info.append(week_0809)
		if week_10 not in week_info:
			week_info.append(week_10)
		if week_1112 not in week_info:
			week_info.append(week_1112)
		if week_13 not in week_info:
			week_info.append(week_13)

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
		week_0102 = re.findall(r'[(](.*?)[)]', each.lesson_0102)
		week_0304 = re.findall(r'[(](.*?)[)]', each.lesson_0304)
		week_05 = re.findall(r'[(](.*?)[)]', each.lesson_05)
		week_0607 = re.findall(r'[(](.*?)[)]', each.lesson_0607)
		week_0809 = re.findall(r'[(](.*?)[)]', each.lesson_0809)
		week_10 = re.findall(r'[(](.*?)[)]', each.lesson_10)
		week_1112 = re.findall(r'[(](.*?)[)]', each.lesson_1112)
		week_13 = re.findall(r'[(](.*?)[)]', each.lesson_13)
		if week_0102 not in week_info:
			week_info.append(week_0102)
		if week_0304 not in week_info:
			week_info.append(week_0304)
		if week_05 not in week_info:
			week_info.append(week_05)
		if week_0607 not in week_info:
			week_info.append(week_0607)
		if week_0809 not in week_info:
			week_info.append(week_0809)
		if week_10 not in week_info:
			week_info.append(week_10)
		if week_1112 not in week_info:
			week_info.append(week_1112)
		if week_13 not in week_info:
			week_info.append(week_13)

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
		week_0102 = re.findall(r'[(](.*?)[)]', each.lesson_0102)
		week_0304 = re.findall(r'[(](.*?)[)]', each.lesson_0304)
		week_05 = re.findall(r'[(](.*?)[)]', each.lesson_05)
		week_0607 = re.findall(r'[(](.*?)[)]', each.lesson_0607)
		week_0809 = re.findall(r'[(](.*?)[)]', each.lesson_0809)
		week_10 = re.findall(r'[(](.*?)[)]', each.lesson_10)
		week_1112 = re.findall(r'[(](.*?)[)]', each.lesson_1112)
		week_13 = re.findall(r'[(](.*?)[)]', each.lesson_13)
		if week_0102 not in week_info:
			week_info.append(week_0102)
		if week_0304 not in week_info:
			week_info.append(week_0304)
		if week_05 not in week_info:
			week_info.append(week_05)
		if week_0607 not in week_info:
			week_info.append(week_0607)
		if week_0809 not in week_info:
			week_info.append(week_0809)
		if week_10 not in week_info:
			week_info.append(week_10)
		if week_1112 not in week_info:
			week_info.append(week_1112)
		if week_13 not in week_info:
			week_info.append(week_13)

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
		week_0102 = re.findall(r'[(](.*?)[)]', each.lesson_0102)
		week_0304 = re.findall(r'[(](.*?)[)]', each.lesson_0304)
		week_05 = re.findall(r'[(](.*?)[)]', each.lesson_05)
		week_0607 = re.findall(r'[(](.*?)[)]', each.lesson_0607)
		week_0809 = re.findall(r'[(](.*?)[)]', each.lesson_0809)
		week_10 = re.findall(r'[(](.*?)[)]', each.lesson_10)
		week_1112 = re.findall(r'[(](.*?)[)]', each.lesson_1112)
		week_13 = re.findall(r'[(](.*?)[)]', each.lesson_13)
		if week_0102 not in week_info:
			week_info.append(week_0102)
		if week_0304 not in week_info:
			week_info.append(week_0304)
		if week_05 not in week_info:
			week_info.append(week_05)
		if week_0607 not in week_info:
			week_info.append(week_0607)
		if week_0809 not in week_info:
			week_info.append(week_0809)
		if week_10 not in week_info:
			week_info.append(week_10)
		if week_1112 not in week_info:
			week_info.append(week_1112)
		if week_13 not in week_info:
			week_info.append(week_13)

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
		week_0102 = re.findall(r'[(](.*?)[)]', each.lesson_0102)
		week_0304 = re.findall(r'[(](.*?)[)]', each.lesson_0304)
		week_05 = re.findall(r'[(](.*?)[)]', each.lesson_05)
		week_0607 = re.findall(r'[(](.*?)[)]', each.lesson_0607)
		week_0809 = re.findall(r'[(](.*?)[)]', each.lesson_0809)
		week_10 = re.findall(r'[(](.*?)[)]', each.lesson_10)
		week_1112 = re.findall(r'[(](.*?)[)]', each.lesson_1112)
		week_13 = re.findall(r'[(](.*?)[)]', each.lesson_13)
		if week_0102 not in week_info:
			week_info.append(week_0102)
		if week_0304 not in week_info:
			week_info.append(week_0304)
		if week_05 not in week_info:
			week_info.append(week_05)
		if week_0607 not in week_info:
			week_info.append(week_0607)
		if week_0809 not in week_info:
			week_info.append(week_0809)
		if week_10 not in week_info:
			week_info.append(week_10)
		if week_1112 not in week_info:
			week_info.append(week_1112)
		if week_13 not in week_info:
			week_info.append(week_13)

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
		week_0102 = re.findall(r'[(](.*?)[)]', each.lesson_0102)
		week_0304 = re.findall(r'[(](.*?)[)]', each.lesson_0304)
		week_05 = re.findall(r'[(](.*?)[)]', each.lesson_05)
		week_0607 = re.findall(r'[(](.*?)[)]', each.lesson_0607)
		week_0809 = re.findall(r'[(](.*?)[)]', each.lesson_0809)
		week_10 = re.findall(r'[(](.*?)[)]', each.lesson_10)
		week_1112 = re.findall(r'[(](.*?)[)]', each.lesson_1112)
		week_13 = re.findall(r'[(](.*?)[)]', each.lesson_13)
		if week_0102 not in week_info:
			week_info.append(week_0102)
		if week_0304 not in week_info:
			week_info.append(week_0304)
		if week_05 not in week_info:
			week_info.append(week_05)
		if week_0607 not in week_info:
			week_info.append(week_0607)
		if week_0809 not in week_info:
			week_info.append(week_0809)
		if week_10 not in week_info:
			week_info.append(week_10)
		if week_1112 not in week_info:
			week_info.append(week_1112)
		if week_13 not in week_info:
			week_info.append(week_13)

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
	week_change = ['4,5,6,7,8,9,10,14,15,16,17', '1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17', '4,5,6,7,8,9,10,11,14,15,16,17', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '', '2,3,4,5,6,7,9,10,11,12,13,14,15,16', '1,2', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,6,7,8,9', '3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,6,7,8,9,11,12,14,15,17', '1,2,3,4,5,6,7,8,9,10,11,12,13', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16', '1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,3,5,7,9,11,13,15,17', '4,6,8,10,12,14,16', '4,5,6,7,8,9,10,13,14,15,16', '5,6,7,8,9,10,11,12,13,14,15,16', '5,10,13,16,4,9,12,15,6,11,14,17', '11,12,13,14,15,16,17', '6,11,14,17,5,10,13,16', '1,2,3,4,5,6,7,8,9', '4,9,12,15,6,11,14,17', '6,11,14,17', '4,6,8,10,12,14,16', '1,2,3,4,5,6,7,8', '5,10,13,16', '1,2,3,4,5,6,7,8,11,12,13,14,15', '1,2,3,4,5,6,7,8,9,11,12,13,14', '9,10,11,12,13,14,15,16,17', '1,2,3,4,5,6,7,8,9,11,12,13', '9,10,11,12,13,14,15,16', '2,3,4', '9,10,11,12', '3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '4,5,6,7,8,9,10,11,13,14,15,16', '2,4,6,8,10,12,14,16', '4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,5,6,7,8,10,11,13,14,16,17', '1,2,3,4,5,7,8,9,10,12,13,15,16', '1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17', '3,4,5,6,7,8,9,10,11,12,13,14,16,17', '3,4,5,6,7,8,9,10,11,12,13,14', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,5,6,7,8,9,10', '1,2,3,4,5,6,7,8,14,15,16,17', '5,6,7,8,9,10,11,12,16,17', '4,5,6,7,8,9,10,11,12,13,14,15','1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,3,5,7,9,11,13,15,17', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16', '12,13,14,15', '4,5,6,7,8,9,10', '5,6,7,8', '13,14,15,16,5,6,7,8', '1,2,3,4,5,8,9,10,11', '1,2,3,4,5', '5,6,7,8,9,10,11,12','1,2,3,4,5,6,7,8,9,10,15,16,17', '1,2,4,5,6,7,8,9', '1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,5,6,7,8,9,10,11,12', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16', '1,2,3,4,6,7,9,11,12,13,14,15,16,17', '1,2,3,4,6,7,9,10,11,12','1,2,3,4,5,6,7,8,9,10,11,12,15,16,17','1,2,3,4,5,6,9,10,11,12','9,10,11,12,13,14,15,16', '5,6,7,8,12,13,14,15,16,17', '1,2,3,4', '1,2,3,4,5,6,7,8', '2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17', '1,2,3,4,5,6', '4,5,6,7,8,9,10,11,14,15,16,17', '2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17','13,14,15,16', '1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17','1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17']
	week_info = []
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
	print(week_info)
	print(len(week_info))

