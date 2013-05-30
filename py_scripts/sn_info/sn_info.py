#!/usr/bin/env python3
import csv
import pprint
import datetime

infile = 'sninc.csv'

def snstats(sninc):
	line_count = sum(1 for line in open(sninc,'r')) - 1
	f = open(sninc,'r')
	csvfile = csv.reader(f)
	header =  csvfile.__next__()
	for i in range(len(header)):
		vars()[header[i] + '_col'] = i
	for elt in header:
		vars()[elt + '_dict'] = {}
		print(elt + '_dict',vars()[elt + '_dict'])
	print(contact_type_dict)
	rep_set = set()
	date_set = set()
	for row in csvfile:
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
	# prints dicts with <= 10 keys
	for heading in header:
		if len(vars()[heading + '_dict']) <= 10:
			pprint.pprint(vars()[heading + '_dict'])
		else:
			pass
	f.close()
	rep_count = len(rep_set)
	date_count = len(date_set)
	print('date_count: ',date_count)
	# adds "Total" key to each dict
	for heading in header:
		vars()[heading + '_dict']['Total'] = line_count
	# prints stuff
	for j in [1,rep_count]:
		for ctype in sorted(contact_type_dict.keys()):
			for i in [1,7,28]:
				new_rate = contact_type_dict[ctype] * i * j / (date_count * rep_count)
				new_thing = ctype + ' inc per %d day per %d rep: %f\n' % (i,j,new_rate)
				print(new_thing)
snstats(infile)
