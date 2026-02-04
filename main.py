# main.py
# ...Main OO Program
from OOP.file_handler import FileHandler

filename = "inventory.csv"
inventory_file = FileHandler(filename)
rows = inventory_file.read()
print(f"#### {inventory_file} ####")
for row in rows:
    print(row)
print(f"#### {inventory_file} ####")
