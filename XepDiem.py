#!/usr/bin/env python3
# -*- coding: utf-8 -*-


definition = {
	"0":6,
	"1":2,
	"2":5,
	"3":5,
	"4":4,
	"5":5,
	"6":6,
	"7":3,
	"8":7,
	"9":6,
	"+":2,
	"-":1,
	"=":2
}

bienThe = {
	"0":[0,6,8,9],
	"1":[1,7],
	"2":[2,3],
	"3":[2,3,5,9],
	"4":[4],
	"5":[3,5,6,9],
	"6":[0,5,6,8,9],
	"7":[1,7],
	"8":[0,6,8,9],
	"9":[0,3,5,6,8,9]
}

def soDiem(data):
	queDiem = 0
	for char in data:
		if char in definition :
			queDiem = queDiem + definition[char]
	return(queDiem)

def demKiTu(x):
	number = []
	for i in data:
		try:
			if i in definition:
				number.append(i)
		except:
			continue
	return(number)

def soSanh(a,b):
	for i in a:
		if i in b:
			b.remove(i)
	if len(b) in [1,2]:
		return(True)
	else:
		return(False)

print("\t\t\t","Author: Qh3xg3m")

while True:
	print()
	data = str(input("\t> Input: "))
	output = []
	for i in bienThe[demKiTu(data)[0]]:
		for j in bienThe[demKiTu(data)[2]]:
			String = "{0} {1} {2} = {3}".format(i,"+",j,i+j)
			if i+j in range(10):
				output.append(String)
			String = "{0} {1} {2} = {3}".format(i,"-",j,i-j)
			if i-j in range(10):
				output.append(String)
	for i in output: 
		temp = i.split(" ")
		if soDiem(data)==soDiem(i) and soSanh(data,temp)==True:
			print("\t",i)
		else:
			continue
 
