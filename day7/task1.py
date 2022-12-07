myfile = open('data1.txt','r')
data = myfile.read()
data = data.split('\n')
change_dir  = '$ cd'
remove_dir = '$ cd ..'
count_add_dir = 0

present_dir_file = []
present_file_index = 0
for i in range(len(data)):
    if change_dir in data[i] and  remove_dir not in data[i] :
        count_add_dir += 1
        
        present_dir_file.append([])
        present_dir_file[present_file_index].append(data[i])
        position = i + 1
        while True:
            if position == len(data):
                count_add_dir = 0
                break
            if change_dir in data[position] and  remove_dir not in data[position] :
                count_add_dir += 1
            if remove_dir in data[position]:
                count_add_dir -= 1
            if count_add_dir == 0:
                count_add_dir = 0
                break

            
            present_dir_file[present_file_index].append(data[position])
            position += 1
        present_file_index += 1

sumation =0
normal = []
for i in present_dir_file:
    temp = 0 
    for each_value in i :
        if '$' in each_value or 'dir' in each_value:
            pass
        else:
            temp += int(each_value.split(' ')[0])
    normal.append([each_value[0],temp])
    if temp <= 100000:

        sumation += temp

print(sumation)


            

