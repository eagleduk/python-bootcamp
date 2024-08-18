## Scope

- 함수 내부에서 외부의 변수와 같은 이름의 변수를 선언해도 외부의 값은 변하지 않는다
- 타 언어(Java, Javascript, C) 등은 새로운 변수 선언을 타입과 같이 하는데 파이썬은 타입 선언을 안하기 떄문에 기존 변수의 값 변경이 아니라 새로운 변수 선언이 되는 듯 하다.

```python
variable = 2

def setValue():
    variable = 5
    print(variable)
    # 5
    
setValue()
print(variable)
# 2
```

- `if`, `for`, `while` 문 내에서 만든 변수는 해당 함수 외부에서도 사용 가능하다
- 블록 범위의 변수라는게 적용되지 않는듯

```python
result = 5
def set_variable():
    if result < 5:
        message = "Less than 5"
    print(message)
```

- 전역변수를 수정할 때에는 `global` 변수라는걸 명시해 주어야 한다.
- 파이썬에서는 전역변수를 쉽게 수정하지 못하도록 되어있다.
- 상수로 된 전역 변수를 사용하고자 할 때에는 대문자로 구성한다.

```python
number = 1

def increase_number():
    global number
    number += 1
    
def decrease_number():
    return number - 1

increase_number()
number = decrease_number()

```