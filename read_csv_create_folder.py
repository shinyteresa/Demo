import csv
import os

def create_folder(name):
    try:
        os.mkdir(name)
        print(f"Folder '{name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{name}' already exists.")

def read_csv_and_create_folders(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            folder_name = row['name']  # Assuming 'FolderName' is a column in your CSV file
            create_folder(folder_name)

if __name__ == '__main__':
    csv_file = 'sampleprogram.csv'  # Replace with the actual CSV file name
    read_csv_and_create_folders(csv_file)
