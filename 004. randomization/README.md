#### Random Module

```python
import random
```

1. random.randint(a,b)
   - a 와 b 사이의 임의의 수를 반환한다.
2. random.random()
   - 0.000 과 0.999999 사이의 임의의 수를 반환한다.

#### 삼단 논법

```python
print("True" if True else "False")
```

#### List

- 음수 인덱스로 뒤에서 부터 출력이 가능하다.

```python

list = [1,2,3,4,5]

list.append(10)     # [1, 2, 3, 4, 5, 10]

list[-1] # 10

list.extend([4,5,6]) # [1, 2, 3, 4, 5, 10, 4, 5, 6]

print(list.index(3))  # 2

```
