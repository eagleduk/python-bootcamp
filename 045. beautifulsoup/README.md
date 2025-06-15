## [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### 1. read HTML

```python
from bs4 import BeautifulSoup

with open("xxx.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")
print(soup)
```

### 2. find Tags

1. tag로 찾기
    ```python
    print(soup.p)
    print(soup.a)
    ```
   - 찾은 tag의 속성 및 컨텐츠 찾기
    ```python
    print(soup.p.get("class"))
    print(soup.p.text())
    ```
   
2. 일치하는 element 찾기
```python
soup.find(name="")
soup.find_all(name="")
```

3. css selector 정보로 찾기
```python
soup.select_one(selector="")
soup.select(selector="")
```