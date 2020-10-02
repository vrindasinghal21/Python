n = int(input())
a,b = map(int,input().split())
for i in range(n-2):
    c = a+b
    a,b = b,c
print(c)

print(float('inf'))
max_ = float('inf')
f = [0]*max_
n = int(input())
# a,b = map(int,input())
def fib(n):
    if n==0:
        return (0,1)
    k = n//2

    k1 , k2 = fib(k)
    a = k1*(2*k2 - k1)
    b = k1*k1 + k2*k2
    if n%2==0:
        return (a,b)
    else:
        return (b,a+b)
print(fib(n)