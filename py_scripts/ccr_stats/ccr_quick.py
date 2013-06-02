#!/usr/bin/env python3
import csv, datetime

datefile = 'daygoog.csv'
hourfile = 'hourgoog.csv'

f = open(hourfile,'r')
csvfile = csv.reader(f)
csvfile.__next__()
while csvfile.__next__()[0] != '':
    pass
header = csvfile.__next__()
ans_col = header.index('Answered Calls')
hour_count = 0
call_count = 0
next_is_hour = True
for row in csvfile:
    crnt_thing = row[0]
    if crnt_thing == 'Customer Calls':
        break
    elif next_is_hour:
        hour_count += 1
        next_is_hour = False
    elif crnt_thing == 'Group Summary:':
        call_count += int(row[ans_col].replace(',',''))
        next_is_hour = True
    else:
        pass
f.close

g = open(datefile,'r')
csvfile = csv.reader(g)
csvfile.__next__()
while csvfile.__next__()[0] != '':
    pass
header = csvfile.__next__()
ans_col = header.index('Answered Calls')
weekday_dict = {}
date_count = 0
next_is_date = True
for row in csvfile:
    crnt_thing = row[0]
    if crnt_thing == 'Customer Calls':
        break
    elif next_is_date:
        date_count += 1
        date_split = [int(i) for i in crnt_thing.split('/')]
        crnt_date = datetime.date(date_split[2],date_split[0],date_split[1])
        crnt_weekday = crnt_date.weekday()
        next_is_date = False
    elif crnt_thing == 'Group Summary:':
        crnt_calls = int(row[ans_col].replace(',',''))
        if crnt_weekday in weekday_dict:
            weekday_dict[crnt_weekday][0] += crnt_calls
            weekday_dict[crnt_weekday][1] += 1
        else:
            weekday_dict[crnt_weekday] = [crnt_calls,1]
        next_is_date = True
    else:
        pass
g.close
month_count = 4
print(hour_count, call_count, date_count, weekday_dict)

outfile = 'ccr_stats.txt'
h = open(outfile,'w')
h.write('Average calls per month: ' + str(call_count / month_count) + '\n')
h.write('Average calls per week: ' + str((call_count * 7) / date_count) + '\n')
h.write('Average calls per day: ' + str(call_count / date_count) + '\n')
h.write('Average calls per hour: ' + str(call_count / (hour_count * date_count)) + '\n')
h.write('Average calls per day on each weekday (0 is Monday):\n')
for wdcode, calls in weekday_dict.items():
    h.write('Day ' + str(wdcode) + ': ' + str(calls[0] / calls[1]) + '\n')
h.close()
