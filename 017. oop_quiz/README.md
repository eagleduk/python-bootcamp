## class

#### constructor

- class 생성자
- 예약된 **__init__** 함수를 사용한다.

```python
class User:
    def __init__(self [, args...]):
        pass # 추후 내용 추가 할 때, 에러 발생하지 않게 하기 위한 예약어
```

#### self

- 객체의 생성자, 함수에 접근하기 위해 추가되는 파라메터
- 호출한 객체의 속성을 사용하기 위해서는 필수로 추가되어야 한다.

```python
class User:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def welcome(self):
        print(f"Hello, {self.name}!")
```