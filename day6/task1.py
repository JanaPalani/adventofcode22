my_file = open('data.txt','r')
data_move = my_file.read()
string = ''
start = 0
end = 4
for i in range(len(data_move)):
    string = set(data_move[start:end])
    if len(string) == 4:
        print(end)
        break
    else:
        start += 1
        end += 1

