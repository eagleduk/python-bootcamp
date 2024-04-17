## Hangman

#### Step 1

- 무작위 단어 선택
- 입력 문자 값의 존재 여부 확인

#### Step 2

- 입력 단어 체크
```python

str = "str"
# 문자열 str 을 분해하여 List 로 반환한다.
str_list = list(str)
print(str_list)  # ["s", "t", "r"]
```

#### Step 3

- 리스트에 문자열 또는 숫자가 포함되어 있는지 확인

```python

str_list = ["a", "b", "x", "e", "t"]

if "a" in str_list:
    print("'a' is in the str_list.")
else:
    print("'a' is not in the str_list.")

```

#### Step 4

- 남은 목숨이 0 이 될 때까지 반복

#### Step 5

- Module Import
```python

# 모듈만 import
import abe
abe.zxc
abe.iop
# 모듈의 속성만 import
from abe import zxc, iop


```
- 유저 경험 개선