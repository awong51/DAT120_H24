from os.path import exists as does_exist

while True:
    file_name = input('What file du you want to inspect?\n')
    if does_exist(file_name):
        break
    else:
        print("Please write a name of a file in this folder.")

file =  open(file_name, 'r')
line_number = 0

for line in file:
    line_number += 1
    find_def = line.find('def')
    if find_def != -1:
        print(f'Line {line_number}: {line}')
file.close()
