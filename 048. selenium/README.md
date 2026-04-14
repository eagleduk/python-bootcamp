#### selenium

```commandline
(python3 -m) pip install selenium
```

- 동적 web 클롤링을 위한 패키지
- 브라우저를 열고 키보드 및 마우스를 제어 가능하다.

#### options

```python

## 브라우저가 자동으로 닫히는 걸 방지하기 위한 옵션
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
```

#### [find element](https://www.selenium.dev/documentation/webdriver/elements/finders/)

- Web 페이지의 요소를 찾는다.

```python
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.find_element(
    'id' | 'xpath' | 'link text' | 'partial link text' | 'name' | 'tag name' | 'class name' | 'css selector'
)
```