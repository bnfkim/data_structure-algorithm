#일반적 계산방법을 이용하는 방법
def sum(n):
    return (n*(n+1))//2

#재귀함수 사용하는 방법
def sum_self(n):
    if n == 0:
        return 0
    return sum_self(n-1) + n

print(sum(10))
print(sum_self(10))