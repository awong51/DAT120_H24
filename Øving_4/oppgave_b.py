#file_name = input('What file du you want to inspect?')
file_name = 'test_for_oppg_b.py'
file =  open(file_name, 'r')
line_number = 0

for line in file:
    line_number += 1
    find_def = line.find('def')
    if find_def  == 0:
        print(f'Line {line_number}: {line}')
file.close()
