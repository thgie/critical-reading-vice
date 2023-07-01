import os
import csv

def extract_includes(folder_path, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['filename', 'value'])

        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as file:
                    for line in file:
                        if line.strip().startswith('#include'):
                            value = line.strip().split('#include')[1].strip().replace('"','')
                            writer.writerow([file_name, value])

folder_path = 'src/'
csv_file_path = '../output/vice-network.csv'

extract_includes(folder_path, csv_file_path)
