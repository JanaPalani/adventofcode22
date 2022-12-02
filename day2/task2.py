my_file = open('day2.txt','r')
data = my_file.read()
data=data.split('\n')
for i in range(len(data)):
    data[i] = data[i].split(' ')
symbols = {'X':1,'Y':2,'Z':3}
draw = {'A':'X','B':'Y','C':'Z'}
winnig = {'A':'Y','B':'Z','C':'X'}
lossing = {'A':'Z','B':'X','C':'Y'}
# score = {'X':0,'Y':3,'Z':6}
sumation = 0
for i in data:
    if i[1] == 'X':
        add = 0 +  symbols[lossing[i[0]]]
    elif i[1] == 'Y':
        add = 3 + symbols[draw[i[0]]]
    elif i[1] == 'Z':
        add = 6 + symbols[winnig[i[0]]]
    sumation += add
print(sumation)
    
