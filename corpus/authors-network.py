import os
import csv

def extract_authors(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    authors = []
    written_by = False
    for i, line in enumerate(lines):
        if "\\author" in line:
            author = line.replace("* \\author ", "").strip()
            authors.append(author)
        elif "Written by" in line:
            written_by = True
            continue
        elif written_by and "<" in line:
            author = line.replace("* ", "").strip()
            authors.append(author)
        elif written_by and "<" not in line:
            written_by = False

    return authors

def process_folder(folder_path, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                authors = extract_authors(file_path)
                if authors:
                    for author in authors:
                        writer.writerow([filename, author])

folder_path = 'src/'
output_file = '../output/authors-network.csv'
process_folder(folder_path, output_file)
