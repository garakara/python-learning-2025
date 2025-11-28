import sys
input = sys.stdin.readline

def solve(n):
    i, num, count = 0, 0, 0
    
    while num <= n:
        a = []
        i = num

        while i > 0:
            a.append(i % 10)
            i //= 10
        
        if 1 not in a and 2 not in a and 4 not in a and 6 not in a and 8 not in a and 9 not in a and 0 not in a:
            if 3 in a and 5 in a and 7 in a:
                count += 1
        
        num += 1

    return(count)

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    print(solve(n))