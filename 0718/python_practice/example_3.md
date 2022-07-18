## 예제 03. [오류 해결] 입력 받기

> 두 수를 Input으로 받아 합을 구하는 코드이다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

### 오류 코드

```python
numbers = input().split()
print(sum(numbers))
```

### Input

```
10 20
```

### Output

```
30
```

## 접근 방법

input().split() 의 값이 문자열이 담긴 리스트라서 정상적인 수행이 되지 않는다. 따라서 map, int 함수를 사용해서 숫자값으로 바꾸어야 한다.

## 코드

```python
numbers = list(map(int, input().split()))
print(sum(numbers))
```

## 느낀점

<aside> 💡 새롭게 알게된 점, 어려웠던 점</aside>

없습니다.