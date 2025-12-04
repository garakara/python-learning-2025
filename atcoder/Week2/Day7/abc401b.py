n = int(input())
flag = False
error_times = 0

for i in range(n):
    atack = input()

    if atack == "login":
        flag = True
        
    elif atack == "logout":
        flag = False
        
    elif atack == "private" and flag == False:
        error_times += 1
        
print(error_times)