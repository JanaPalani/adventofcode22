my_file = open('data.txt','r')
data = my_file.read()
data=data.split('\n')
for i in range (len(data)):
    data[i] = data[i].split(',')
    data[i][0] = data[i][0].split('-')
    data[i][1] = data[i][1].split('-')
sumation  = 0
print(data)

for i in range(len(data)):
    data[i][0] = set(range(int(data[i][0][0]), int(data[i][0][1])+1))
    data[i][1] = set(range(int(data[i][1][0]), int(data[i][1][1])+1))
    get = data[i][0].intersection(data[i][1])
    
    if len(list(get)) >= 1:
        sumation += 1
print(sumation)
# {26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 
# 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 
# 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 
# 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80}

    # for i in data[i][0]:
    #     if i in data[i][1]:
    #         sumation+= 1
    #         break
    #     else:
    #         continue
    # else:
    #     for i in data[i][1]:
    #         if i in data[i][0]:
    #             sumation+= 1
    #             break
    #         else:
    #             continue




