#### exception

- try, except, else, finally 를 사용하여 에러 발생시 동작을 취할 수 있다.
  - `try` 수행 하려는 메인 로직
  - `except` 에러 발생 시 수행 하려는 로직
  - `else` 수행 하려는 메인 로직에서 에러가 발생하지 않았을 때 수행되는 로직
  - `finally` 에러가 있건 없건 무조건 수행되는 로직

```python
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
```

- `except` 항목에는 처리하고자 하는 에러를 항목별로 구현할 수 있다.

```python
try:
    pass
except FileNotFoundError as message:
    pass
except TypeError as message:
    pass
except KeyError as message:
    pass
```