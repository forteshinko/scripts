#!/usr/bin/env python3
import csv,datetime

infile = 'sn_new.csv'
outfile = 'sn_info.txt'

line_count = sum(1 for line in open(infile,'r')) - 1
f = open(infile,'r')
csvfile = csv.reader(f)
header = csvfile.__next__()
for i in range(len(header)):
	vars()[header[i] + '_col'] = i
for elt in header:
	vars()[elt + '_dict'] = {}
rep_set = set()
date_set = set()
for row in csvfile:
    if row[contact_type_col] == 'Phone':
    	for i in range(len(header)):
    		crnt_thing = row[i]
    		crnt_heading = header[i]
    		crnt_dict = vars()[crnt_heading + '_dict']
    		# increments occurrence of thing
    		if crnt_thing in crnt_dict:
    			crnt_dict[crnt_thing] += 1
    		else:
    			crnt_dict[crnt_thing] = 1
    		# adds rep to the rep_set
    		if crnt_heading == 'assigned_to':
    			rep_set.add(crnt_thing)
    		# adds date to date_set
    		elif crnt_heading == 'sys_created_on':
    			date_str_list = crnt_thing.split()[0].split('-')
    			date_list = [int(i) for i in date_str_list]
    			date = datetime.date(*date_list)
    			date_set.add(date)
f.close()
rep_count = len(rep_set)
date_count = len(date_set)
# prints stuff
for j in [1,rep_count]:
	for ctype in sorted(contact_type_dict.keys()):
		for i in [1,7,28]:
			new_rate = contact_type_dict[ctype] * i * j / (date_count * rep_count)
			new_thing = ctype + ' inc per %d day per %d rep: %f\n' % (i,j,new_rate)
			print(new_thing)
month_dict = {}
hour_dict = {}
weekday_dict = {}
for dtime, calls in sys_created_on_dict.items():
    dtime_split = dtime.split()
    day_str_split = dtime_split[0].split('-')
    day_split = [int(i) for i in day_str_split]
    time_str_split = dtime_split[1].split(':')
    time_split = [int(i) for i in time_str_split]
    crnt_date = datetime.date(*day_split)
    crnt_time = datetime.time(*time_split)
    crnt_month = crnt_date.month
    crnt_hour = crnt_time.hour
    crnt_weekday = crnt_date.weekday()
    if crnt_month in month_dict:
        month_dict[crnt_month] += calls
    else:
        month_dict[crnt_month] = calls
    if crnt_hour in hour_dict:
        hour_dict[crnt_hour] += calls
    else:
        hour_dict[crnt_hour] = calls
    if crnt_weekday in weekday_dict:
        weekday_dict[crnt_weekday][0] += calls
        weekday_dict[crnt_weekday][1] += 1
    else:
        weekday_dict[crnt_weekday] = [calls,1]
print(weekday_dict)
month_count = len(month_dict)
hour_count = len(hour_dict)
month_avg = line_count/month_count
week_avg = (line_count * 7)/date_count
day_avg = line_count/date_count
hour_avg = line_count/(date_count * hour_count)
g = open(outfile,'w')
g.write('Avg incs per month:\n')
monthcodes = {1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April',
5 : 'May', 6 : 'June', 7 : 'July', 8 : 'August', 9 : 'September',
10 : 'October', 11 : 'November', 12 : 'December'}
for month, calls in month_dict.items():
    g.write(str(monthcodes[month]) + ': ' + str(calls) + ' calls\n')
g.write('Avg calls per month: ' + str(month_avg) + '\n')
g.write('Avg calls per week: ' + str(week_avg) + '\n')
g.write('Avg calls per day: ' + str(day_avg) + '\n')
g.write('Avg calls for each weekday:\n')
daycodes = {0 : 'Monday', 1 : 'Tuesday', 2 : 'Wednesday',
3 : 'Thursday', 4 : 'Friday', 5 : 'Saturday', 6 : 'Sunday'}
for weekday, infolist in weekday_dict.items():
    print(infolist)
    g.write(daycodes[weekday] + ': ' + str(infolist[0]/infolist[1]) + '\n')
g.write('Avg calls per hour: ' + str(hour_avg) + '\n')
g.close()
