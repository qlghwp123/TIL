## 예제 06. [오류 해결] 1부터 N까지의 2의 곱 저장하기

> 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

### 오류 코드

```python
N = 10
answer = ()
for number in range(N + 1):
    answer.append(number * 2)

print(answer)
```

### Output

```
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## 접근 방법

answer 는 현재 빈 튜플로 초기화가 되있으므로 리스트로 초기화 해준다.

## 코드

```python
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)
```

## 느낀점

<aside> 💡 새롭게 알게된 점, 어려웠던 점</aside>

없습니다.