## [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### 1. read HTML

```python
from bs4 import BeautifulSoup

with open("xxx.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")
print(soup)
```
