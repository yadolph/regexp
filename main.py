import csv
from pprint import pprint
import re


with open('phonebook_raw.csv') as f:
    rows = csv.reader(f,delimiter=',')
    contacts_list = list(rows)

for row in contacts_list[1:]:
    pattern = re.compile(r'\+*7*8*\s*\(*(\d{3})-*\)*\s*(\d{3})-*\s*(\d{2})-*\s*(\d+)')
    row[-2] = pattern.sub(r'+7(\1)-\2-\3-\4', row[-2])

for row in contacts_list[1:]:
    pattern = re.compile(r'\(*(доб\.)\s(\d{4})\)*')
    row[-2] = pattern.sub(r'\1\2', row[-2])

for row in contacts_list[1:]:
	full_name = row[0] + ' ' + row[1] + ' ' + row[2]
	full_name_list = full_name.split(' ')
	row[0] = full_name_list[0]
	row[1] = full_name_list[1]
	row[2] = full_name_list[2]

temp_list = []

for row in contacts_list[1:]:
	temp_list = [i for i in contacts_list if i != row]
	for temp_row in temp_list:
		if row[0] == temp_row[0]:
			temp_list.remove(temp_row)



with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)


with open("phonebook__.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(temp_list)  



#pprint(contacts_list)

