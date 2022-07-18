## 예제 08. [오류 해결] 모음의 개수 찾기

> 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

### 오류 코드

```python
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u":
        count += 1

print(count)
```

### Output

```
3
```

## 접근 방법

A or B 에서 A 에 0 이 아닌 “값” 이 올 경우 항상 참으로 간주한다. 따라서 비교 연산자인 “==” 를 사용하는 것이 올바르다.

## 코드

```python
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)
```

## 느낀점

<aside> 💡 새롭게 알게된 점, 어려웠던 점</aside>

없습니다.