def solve():
    s = input()
    digits = [int(d) for d in s]
    
    def dfs(index, current_sum, expression):
        if index == 4:  # 何を入れる?
            if current_sum == 7:
                print(expression + "=7")
                return True
            return False
        
        next_digit = digits[index]
        
        # +を試す
        if dfs(index + 1, current_sum + next_digit, expression + "+" + str(next_digit)):  # 何を入れる?
            return True
        
        # -を試す
        if dfs(index + 1, current_sum - next_digit, expression + "-" + str(next_digit)):  # 何を入れる?
            return True
        
        return False
    
    dfs(1, digits[0], str(digits[0]))

solve()