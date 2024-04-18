#### functions with inputs

- 함수에 정의한 변수는 `Parameter`
- 함수에 전달하는 값은 `Argument`

```python
def my_function(something):
    #Do this with something
    #Then do this with something
    #Finally do this
```

#### location Arguments

- 함수에 인자를 전달할 때, 파라메터 순으로 전달
```python
def my_function(a,b,c):
    #Do this with a
    #Then do this with b
    #Finally do this with c

my_function(1,2,3)
```

#### Keyword Arguments

- 함수에 인자를 전달할 때, 파라메터 명으로 전달
```python
def my_function(a,b,c):
    #Do this with a
    #Then do this with b
    #Finally do this with c

my_function(c=3,a=1,b=2)
```