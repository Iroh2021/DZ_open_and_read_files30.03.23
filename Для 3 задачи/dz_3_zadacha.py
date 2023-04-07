import os
current = os.getcwd()
folder_name = 'Для 3 задачи'
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
full_path_1 = os.path.join(current, folder_name, file_name_1)
full_path_2 = os.path.join(current, folder_name, file_name_2)
full_path_3 = os.path.join(current, folder_name, file_name_3)
txt_list = [file_name_1, file_name_2, file_name_3]
txt_list_count = []
for i in txt_list:
    with open(i, 'rt', encoding='utf-8') as file:
       file_list = file.readlines()
       count = 1
       for n in file_list:
           if '\n' in n:
               count += 1
    txt_list_count.append(count)
txt_dict = dict(zip(txt_list, txt_list_count))
txt_list_count = sorted(txt_list_count)
for i in txt_list_count:
    for v, k in txt_dict.items():
        if i == k:
            print(v)
            print(txt_dict[v])
            with open(v, 'rt', encoding='utf-8') as file:
                print(file.read())
                