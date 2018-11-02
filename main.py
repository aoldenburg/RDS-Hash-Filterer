import sys
import csv

args = sys.argv
input_file = args[1]
output_file = args[2]
image_types = {'.gif', '.tiff', '.bmp', '.jpg', '.png', '.tif', '.RAW', '.svg'}
filtered_rows = []
print('reading file' + input_file + ', this may take some time..')
with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for row in csv_reader:
        file_name = row[3]
        file_ext_idx = file_name.rfind('.')
        file_ext = file_name[file_ext_idx:].lower()
        if file_ext in image_types:
            filtered_rows.append(row)
print('finished filtering, now writing..')
with open(output_file, 'w') as csv_file:
    csv_writer = csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for row in filtered_rows:
        csv_writer.writerow(row)