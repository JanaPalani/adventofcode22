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


normal = []
for i in present_dir_file:
    temp = 0 
    for each_value in i :
        if '$' in each_value or 'dir' in each_value:
            pass
        else:
            temp += int(each_value.split(' ')[0])
    normal.append([i[0],temp])
total_system =70000000

final_list = []
dir_space = total_system - normal[0][1]
should_free = 30000000 - dir_space
for i in normal:
    if i[1] >= should_free:
        final_list.append(i)
final_list.sort(key= lambda x :x [1])
print(final_list[0][1])
