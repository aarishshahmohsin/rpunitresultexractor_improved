import csv
from scraper import fetch_cpi
import os

csv_file = "students.csv"
output_file = "output.csv"

if (not os.path.exists):
    os.system("touch {}".format(output_file))

with open('output.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    with open(csv_file) as file_obj:
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            faculty_no = row[0]
            enrolment_no = row[1]
            cpi_arr = fetch_cpi(faculty_no, enrolment_no)
            output_array = row
            for i in cpi_arr:
                output_array.append(i)
            writer.writerow(output_array)
            print(output_array)
