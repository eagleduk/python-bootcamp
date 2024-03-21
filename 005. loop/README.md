#### 배열(List) 를 사용하는 반복문

```python
arr = [1,2,3,4,5]

for num in arr:
    print(num)
    # 1
    # 2
    # 3
    # 4
    # 5

```

#### 범위(range) 를 사용하는 반복문

- range(start, end[, step])
- end 값은 포함되지 않는다.

```python
for num in range(1, 11, 2):
    print(num)
    # 1
    # 3
    # 5
    # 7
    # 9
```

#### random

- random.choice([])  
  : 제공된 배열 안에서 무작위 값을 추출한다.
- random.shuffle([])  
  : 제공된 베열을 무작위로 섞는다.

```python
import random

arr = ["a", "b", "c", "d"]

random_char = random.choice(arr)

random.shuffle(arr)

```

#### List

- 항목 추가  
  : append()  
  : `+=`

```python
arr = []

arr.append(1)   # [1]

arr += 2        # [1,2]

```
