import os
import sys
import re

data = sys.stdin.readlines()

list = ''
for row in data:
    rows = row.lower()
    x = re.sub(r"\D", "", rows)
    c = ','
    list += x + ','
    # print(f"{x}")
    list1 = list.replace(',,', ',')
    list2 = list1[:-1]

print(list2)
# print('asn numbers with comman no space example 4543,45654,8765')
# ASN = input()
os.system(f"amass intel -asn {list2}")
