## File System

#### read

- 파일을 열어 변수에 대입하면, 파일 변수를 닫아주어야 한다.

```python
file = open([파일명])
contents = file.read()
file.close()
```

- `with` 키워드를 사용하여 해당 함수가 끝나면 파일을 자동으로 닫아준다.

```python
with open([파일명]) as file:
    contents = file.read()
```

#### write

- 파일을 쓰기 위해서는 `a(append)` 또는 `w(write)` 모드를 사용한다.
- `a` 는 추가, `w`는 덮어쓰기 모드 이다.

```python
file = open([파일명], mode="a(w)")
file.write("New Text")
file.close()
```

```python
with open([파일명], mode="a(w)") as file:
    file.write("new text")
```