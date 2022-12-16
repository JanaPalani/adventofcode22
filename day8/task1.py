my_file = open('data.txt','r')
data = my_file.read()
data = data.split('\n')
for i in range(len(data)):
    data[i] = list(data[i])
    data[i] = list(map(int,data[i]))
visible_trees = []

# for top view:
top_view_trees = []
view_indexes = []
for i in range(len(data[0])):
    large = -1
    for j in range(len(data)):
        if data[j][i] > large:
            top_view_trees.append([data[j][i],(j,i)])
            view_indexes.append((j,i))
            large = data[j][i]

print(top_view_trees)



# for bottom view:
bottom_to_top = [i for i in range(len(data[0])-1,-1,-1)]
bottom_view_trees = []
for i in range(len(data[0])):
    large = -1
    for j in bottom_to_top:
        if data[j][i] >large:
            if (j,i) not in view_indexes:
                bottom_view_trees.append([data[j][i],(j,i)])
                view_indexes.append((j,i))
            large = data[j][i]
print(bottom_view_trees)


left_to_right = [i for i in range(len(data[0]))]
left_view_trees = []
for i in range(len(data)):
    large = -1
    for j in left_to_right:
        if data[i][j] >large:
            if (i,j) not in view_indexes:
                left_view_trees.append([data[i][j],(i,j)])
                view_indexes.append((i,j))
            
            large = data[i][j]
print(left_view_trees)


right_to_left = [i for i in range(len(data[0])-1, -1,-1)]
right_view_trees = []
for i in range(len(data)):
    large = -1
    for j in right_to_left:
        if data[i][j] >large:
            if (i,j) not in view_indexes:
                left_view_trees.append([data[i][j],(i,j)])
                view_indexes.append((i,j))
            
            large = data[i][j]
print(right_view_trees)
print(len(top_view_trees)+len(bottom_view_trees)+len(left_view_trees)+len(right_view_trees))



