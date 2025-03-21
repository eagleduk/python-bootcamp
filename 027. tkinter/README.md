#### Tkinter

- [TK Options](https://www.tcl-lang.org/man/tcl8.6.13/TkCmd/contents.htm)
- Widget 들을 화면에 표현할때, `pack`, `place`, `grid`로 위치를 지정할 수 있다.
  - pack 은 화면의 상,하,좌,우 로 위치시킨다.
  - place 는 구체적인 좌표(x,y)로 위치시킨다.
  - grid 는 행과 열을 사용하여 위치시킨다.

#### Default Arguments

- 함수에서 사용하고자 하는 인자에 대한 초기값을 설정할 수 있다

```python
def log(text="Hello"):
    print(text)

log("Hi")
```

#### Unlimited Arguments

- 함수에서 사용하고자 하는 인자의 갯수에 대하여 제한없이 사용할 수 있다.

```python
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

add(1,2,3,4,5,6,7,8,9,0,11)
```

#### Keyword Arguments

- 함수에서 사용하고자 하는 인자의 갯수에 대하여 정해 놓은 키값을 사용할 수 있다.

```python
def calculate(n, **kwargs):
    n += kwargs.get("sum")
    n -= kwargs.get("sub")
    n *= kwargs.get("mul")
    n /= kwargs.get("div")
    return n

calculate(10, sum=4, sub=3, mul=2, div=2)
```