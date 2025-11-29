import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    digits = [int(d) for d in s]

    def dfs(index, current_sum, exp):
        if index == 4:
            if current_sum == 7:
                print(exp)
                return True
            else:
                return False
            
        next_digits = digits[index]
        
        if dfs(index + 1, current_sum + next_digits, exp + "+" + str(next_digits)):
            return True
        
        if dfs(index + 1, current_sum - next_digits, exp + "-" + str(next_digits)):
            return True
        
        return False
    
    dfs(1, digits[0], str(digits[0]))

if __name__ == '__main__':
    solve()