import os

def count_lines_in_folder(folder_path):
    total_lines = 0

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                total_lines += len(lines)

    return total_lines

folder_path = 'src/'
total_lines = count_lines_in_folder(folder_path)
print("Total lines in the folder:", total_lines)