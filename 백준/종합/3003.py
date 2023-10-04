chess_list = [1, 1, 2, 2, 2, 8]

present_list = list(map(int, input().split()))
need_list =[0]*6
for i in range(len(chess_list)):
    if(i == 0):
        need_list[i] = chess_list[i] - present_list[i]
    elif(i == 1):
        need_list[i] = chess_list[i] - present_list[i]  
    elif(i == 2):
        need_list[i] = chess_list[i] - present_list[i]
    elif(i == 3):
        need_list[i] = chess_list[i] - present_list[i]
    elif(i == 4):
        need_list[i] = chess_list[i] - present_list[i]
    elif(i == 5):
        need_list[i] = chess_list[i] - present_list[i]

for i in need_list:
    print(i,end=" ")
