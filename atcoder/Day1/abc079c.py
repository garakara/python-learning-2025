def solve_abc079c_debug():
    s = input().strip()
    digits = [int(d) for d in s]
    
    def dfs(index, current_sum, expression, depth=0):
        indent = "  " * depth
        print(f"{indent}→ dfs(index={index}, sum={current_sum}, expr='{expression}')")
        
        # 基底条件
        if index == 4:
            if current_sum == 7:
                print(f"{indent}★ 見つかった! {expression}=7")
                print(expression + "=7")
                return True
            else:
                print(f"{indent}✗ {current_sum} != 7")
            return False
        
        next_digit = digits[index]
        
        # +を試す
        print(f"{indent}[+] 次は {next_digit} を足す")
        if dfs(index + 1, 
               current_sum + next_digit, 
               expression + "+" + str(next_digit),
               depth + 1):
            return True
        
        # -を試す
        print(f"{indent}[-] 次は {next_digit} を引く")
        if dfs(index + 1, 
               current_sum - next_digit, 
               expression + "-" + str(next_digit),
               depth + 1):
            return True
        
        print(f"{indent}← どちらもダメだった")
        return False
    
    dfs(1, digits[0], str(digits[0]))

solve_abc079c_debug()