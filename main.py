import csv
from pprint import pprint
import re

def proper_phone_numbers(contacts_list):
	for row in contacts_list[1:]:
	    pattern = re.compile(r'\+*7*8*\s*\(*(\d{3})-*\)*\s*(\d{3})-*\s*(\d{2})-*\s*(\d+)')
	    row[-2] = pattern.sub(r'+7(\1)-\2-\3-\4', row[-2])

	for row in contacts_list[1:]:
	    pattern = re.compile(r'\(*(доб\.)\s(\d{4})\)*')
	    row[-2] = pattern.sub(r'\1\2', row[-2])
	return contacts_list

def proper_names(contacts_list):
	for row in contacts_list[1:]:
		full_name = row[0] + ' ' + row[1] + ' ' + row[2]
		full_name_list = full_name.split(' ')
		row[0] = full_name_list[0]
		row[1] = full_name_list[1]
		row[2] = full_name_list[2]
	return contacts_list

def merge_doubles(contacts_list):
	for row in contacts_list:
		temp_contacts_list = [i for i in contacts_list if i != row]
		for temp_row in temp_contacts_list:
			if temp_row [0] == row[0]:
				for idx, val in enumerate(row):
					if val:
						pass
					else:
						try:
							row[idx] = temp_row[idx]
						except IndexError:
							pass
				contacts_list.remove(temp_row)
	return contacts_list

def main(contacts_list):
	contacts_list = proper_names(contacts_list)
	contacts_list = proper_phone_numbers(contacts_list)
	contacts_list = merge_doubles(contacts_list)
	return contacts_list


if __name__ == '__main__':

	with open('phonebook_raw.csv') as f:
	    rows = csv.reader(f,delimiter=',')
	    contacts_list = list(rows)

	main(contacts_list)

	with open("phonebook.csv", "w") as f:
	  datawriter = csv.writer(f, delimiter=',')
	  datawriter.writerows(contacts_list)

