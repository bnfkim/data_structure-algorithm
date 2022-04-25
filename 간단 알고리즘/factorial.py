#일반적론
def factorial_normal(n):
    first = 1
    # 1부터 n까지 반복
    for i in range(1, n+1):
        first = first * i
    return first

#재귀함수
def factorial(n):
    if n <= 1:
        return 1
    return factorial(n-1) * n

print(factorial_normal(5))
print(factorial(5))