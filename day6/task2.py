my_file = open('data.txt','r')
data_move = my_file.read()
string = ''
start = 0
end = 14
for i in range(len(data_move)):
    string = set(data_move[start:end])
    if len(string) == 14:
        print(end)
        break
    else:
        start += 1
        end += 1

