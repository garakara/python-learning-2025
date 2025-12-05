s = input()
N = list(map(int, s))

def dfs(index, current_sum, exp):
    
    # 1
    if index == 4:
        if current_sum == 7:
            print(exp+"=7")
            return True
        else:
            return False
    # 2
    if dfs(index+1, current_sum + N[index], exp + "+" + str(N[index])):
        return True

    # 3
    if dfs(index+1, current_sum - N[index], exp + "-" + str(N[index])):
        return True
    
    return False
    
dfs(1, N[0], str(N[0]))

