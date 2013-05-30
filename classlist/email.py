#!/usr/bin/python

emaillist = open('.emaillist','w')

for infostr in open(raw_input("Class list file: ")):
	emaillist.write(infostr.split(":")[1][:8] + "@uwaterloo.ca\n")

emaillist.close()
