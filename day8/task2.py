my_file = open('data.txt','r')
data = my_file.read()
data = data.split('\n')
normal_data = []
for i in range(len(data)):
        data[i] = list(data[i])
        data[i] = list(map(int,data[i]))
for i in range(len(data[0])):
    for j in range(len(data)):
        if i== 0 or j == 0 or j == len(data)-1 or i == len(data[0])- 1:
            pass
        else:
            normal_data.append((i,j))
print(normal_data)
score  = 0
for i in normal_data:
    temp = 1
    right_side_num   = 0
    for j in range(1,len(data[0]) - i[1]):
        
        new_tree =  [i[0],i[1]+j]

        if data[new_tree[0]][new_tree[1]] <  data[i[0]][i[1]]:
                right_side_num += 1
        if data[new_tree[0]][new_tree[1]] >=  data[i[0]][i[1]]:

            right_side_num += 1
            break
        

    left_side_num  = 0

    for j in range(1,i[1]+1):
        new_tree = [i[0], i[1]-j]


        if data[new_tree[0]][new_tree[1]] <  data[i[0]][i[1]]:
            # if data[new_tree[0]][new_tree[1]] >= new_left:
                left_side_num += 1
        elif data[new_tree[0]][new_tree[1]] >= data[i[0]][i[1]]:
            left_side_num += 1
            break

    bottom_side_num  = 0

    for j in range (1,len(data) - i[0]):
        new_tree = [i[0]+j,i[1]]

        if data[new_tree[0]][new_tree[1]] <  data[i[0]][i[1]]:
            # if data[new_tree[0]][new_tree[1]] >= new_bottom:
                bottom_side_num += 1
        elif data[new_tree[0]][new_tree[1]] >= data[i[0]][i[1]]:
            bottom_side_num += 1
            break

    top_side_num  = 0  
    for j in range(1,i[0]+1):
        new_tree = [i[0]-j,i[1]]

        if data[new_tree[0]][new_tree[1]] <  data[i[0]][i[1]]:
            # if data[new_tree[0]][new_tree[1]] >= new_top:
                top_side_num += 1
        elif data[new_tree[0]][new_tree[1]] >= data[i[0]][i[1]]:
            top_side_num+= 1
            break


    all_side = [top_side_num,bottom_side_num,left_side_num,right_side_num]

    for k in all_side:

        if k != 0 :
    
            temp *= k

    if temp > score:
        score = temp
print(score)