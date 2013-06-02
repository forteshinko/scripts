#!/usr/bin/env python3
import csv, datetime

infile = 'sn_new.csv'

f = open(infile,'r')
csvfile = csv.reader(f)
header = csvfile.__next__()
contact_col = header.index('contact_type')
date_col = header.index('sys_created_on')
inc_count = 0
date_dict = {}
hour_set = set()
for row in csvfile:
    crnt_contact = row[contact_col]
    datetime_split = row[date_col].split()
    time_str_split = datetime_split[1].split(':')
    time_int_split = [int(i) for i in time_str_split]
    crnt_time = datetime.time(*time_int_split)
    crnt_hour = crnt_time.hour
    if crnt_contact == 'Phone' and 8 <= crnt_hour < 21:
        date_str_split = datetime_split[0].split('-')
        date_int_split = [int(i) for i in date_str_split]
        crnt_date = datetime.date(*date_int_split)
        if crnt_date in date_dict:
            date_dict[crnt_date] += 1
        else:
            date_dict[crnt_date] = 1
        hour_set.add(crnt_hour)
        inc_count += 1
f.close()

weekday_dict = {}
for date, incs in date_dict.items():
    crnt_weekday = date.weekday()
    if crnt_weekday in weekday_dict:
        weekday_dict[crnt_weekday][0] += incs
        weekday_dict[crnt_weekday][1] += 1
    else:
        weekday_dict[crnt_weekday] = [incs, 1]
hour_count = len(hour_set)
month_count = 4
date_count = len(date_dict)
print(hour_count, inc_count, date_count, weekday_dict)

outfile = 'sn_stats.txt'
h = open(outfile,'w')
h.write('Average phone incs per month: ' + str(inc_count / month_count) + '\n')
h.write('Average phone incs per week: ' + str((inc_count * 7) / date_count) + '\n')
h.write('Average phone incs per day: ' + str(inc_count / date_count) + '\n')
h.write('Average phone incs per hour: ' + str(inc_count / (hour_count * date_count)) + '\n')
h.write('Average phone incs per day on each weekday (0 is Monday):\n')
for wdcode, calls in weekday_dict.items():
    h.write('Day ' + str(wdcode) + ': ' + str(calls[0] / calls[1]) + '\n')
h.close()
