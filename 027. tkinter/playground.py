def log(a=1, b=2, c=3):
    print(a, b, c)

log(10)

def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1,2,3,4,5,6,7,8,9,0)

def calculate(n, **kwargs):
    n += kwargs.get("s")
    n -= kwargs.get("a")
    n *= kwargs.get("m")
    n /= kwargs.get("d")
    return n

print(calculate(10, s=2, a=2, m=3, d=4))