import sys
def solve():
    input = sys.stdin.readline
    S = int(input())
    
    if 200 <= S and S <= 299:
        return "Success"
    return "Failure"

if __name__ == '__main__':
    print(solve())