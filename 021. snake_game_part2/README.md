## Part 2

#### Inheritance

```python
class Parent:
    def __init__(self):
        pass

class Child(Parent):
    def __init__(self):
        super().__init__()

```

#### Slice

- 배열, 튜플 뒤에 [a:b:c] 로써 원하는 위치의 값들을 추출할 수 있다.
- `[Start:End:Step]` 순으로, *Start*를 생략하면 처음부터, *End*를 생략하면 마지막까지 *Step*을 생략하면 순차적으로 값을 추출한다.