import os

def write_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        print("Data written to file successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        


def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        print("Data read from file successfully.")
        return data
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
    
search=input("search")
file_path = 'example.txt'

data_from_file = read_from_file('file_path')
if search==data_from_file :
 print(data_from_file)  
else :
 print("Site does not exist")
 add = input("add")
 data_to_write = add
 write_to_file(file_path, data_to_write)
 