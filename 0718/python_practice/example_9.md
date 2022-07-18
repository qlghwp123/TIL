## 예제 09. [오류 해결] 과일 개수 구하기

> 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

### 오류 코드

```python
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)
```

### Output

```
{'Apricot': 1,
 'Blackcurrant': 1,
 'Cantaloupe': 1,
 'Feijoa': 1,
 'Grapefruit': 1,
 'Juniper berry': 1,
 'Salal berry': 1,
 'Soursop': 1}
```

## 접근 방법

fruit_count 에 없으면 fruit 를 추가하는 부분 : fruit_count = {fruit: 1} 이 잘못 됐다. 이 부분은

fruit_count[fruit] = 1 로 바꾸어야 한다.

## 코드

```python
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)
```

## 느낀점

<aside> 💡 새롭게 알게된 점, 어려웠던 점</aside>

없습니다.