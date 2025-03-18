#### List Comprehension

- 기존 list 에서 새로운 list 를 만드는 것.

```python
list = []
new_list = [i for i in list]
```

- 조건을 추가하여 각 항목에 대한 필터를 추가할 수 있다.

```python
list = []
new_list = [i for i in list if test]
```

#### Dictionary Comprehension

```python
dict = {}
new_dict = {item:dict[item] for item in dict}
new_dict_2 = {key:value for (key, value) in dict.items()}
new_dict_3 = {key:value for (key, value) in dict.items() if test}
```
