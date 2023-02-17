import openpyxl
import os
from sys import argv
name_file = argv[1]
print(name_file)
path_file = os.path.abspath(os.curdir)

def main(path_file, name_file):
    list_path_file = []
    for address, dirs, files in os.walk(path_file):
        for name in files:
            if name == name_file:
                list_path_file.append(os.path.join(address, name))

    list_data =[]
    list_hosts =[]
    for path in list_path_file:
        with open(path) as file:
            data = file.read()
            list_data.append(f"<id-{data}>")
            print(data)
            if int(data)<10:
                list_hosts.append(f"<host-0{data}>")
            else:
                list_hosts.append(f"<host-{data}>")
    wb = openpyxl.Workbook()
    ws = wb['Sheet']     
    print(list_data)
    print(list_hosts)
    ws.append(list_hosts)
    ws.append(list_data)
    wb.save("hosts.xlsx")
    wb.close()
    #path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name_file)
    #os.remove(path)

main(path_file,name_file)
