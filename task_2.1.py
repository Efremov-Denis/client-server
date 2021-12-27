import os
import csv

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

folder = 'C:\\Users\\User\\client-server\\Materials_to_tasks'

for item in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, item)):
        data_path = folder + '\\' + item
        with open(data_path, "r") as file:
            text = file.readlines()
            for line in text:
                    if 'Изготовитель системы' in line:
                        data_list1 = line.split(':')
                        os_prod_list.append(data_list1[1])

                    if 'Название ОС' in line:
                        data_list2 = line.split(':')
                        os_name_list.append(data_list2[1])

                    if 'Код продукта' in line:
                        data_list3 = line.split(':')
                        os_code_list.append(data_list3[1])

                    if 'Тип системы' in line:
                        data_list4 = line.split(':')
                        os_type_list.append(data_list4[1])

print(os_prod_list)
print(os_name_list)
print(os_code_list)
print(os_type_list)

with open('kp_data_write.csv', 'w') as f_n:
    f_n_writer = csv.writer(f_n)
    for line in os_prod_list:
        f_n_writer.writerow(line)