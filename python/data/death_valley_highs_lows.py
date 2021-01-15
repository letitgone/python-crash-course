# @Author ZhangGJ
# @Date 2021/01/14 23:18

import csv

filename = '../../python-crash-course/resources/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
