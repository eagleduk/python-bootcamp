#### Basic Data Types

- String
- Integer
  - 숫자 형식의 데이터에서 `_` 표시는 개발자의 가독성을 높여주지만 실제 데이터에는 적용되지 않는다.
- Float
- Boolean

#### type 확인

```python
type(1) # <class 'int'>
type("1") # <class 'str'>
type(True) # <class 'bool'>
type(11.11) # <class 'float'>

```

#### 수학연산

PENDAS

- Parentheses(괄호)
- Exponent(지수)
- Moultiplication(곱셈), Division(나눗셈)
- Addition(덧셈), Subtraction(뺄셈)

#### 소수점 처리

- int() => 소수점 이하의 숫자는 버림
  ```python
  print(8/3) # 2.66666666666666666....
  print(int(8/3)) # 2
  ```
- round() => 입력 숫자 반올림

  ```python

  print(round(2.555555)) # 3
  print(round(2.555555, 2)) # 2.56

  ```

- `a // b` 나눔과 동시에 소수점 이하 숫자 버림(몫 계산)
  ```python
  print(8//3) # 2
  ```

#### f-String

문자열 앞에 **_f_** 를 추가하고 `{}` 안에 변수를 입력하여 다양한 타입을 혼합하여 문자열 포멧을 만들 수 있다.

```python
a = 0
b = True
c = 0.2222

print(f"test {a} / {b} == {c}") # test 0 / True == 0.2222
```

#### 소수점 강제 출력

`"{:.#f}".format([v])` 형태로 [v] 의 값을 **#** 자리수 까지 `0` 으로 채워서 출력해 준다.

```python
print(f"TEST  {"{:.2f}".format(5/2)}")
# TEST  2.50
```
