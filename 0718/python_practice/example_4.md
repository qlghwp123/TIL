## 예제 04. [오류 해결] 입력 받기 - 2

> 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

### 오류 코드

```python
words = list(map(int, input().split()))
print(words)
```

### Input

```
I'm Tuotur 6
```

### Output

```
["I'm", 'Tutor', '6']
```

## 접근 방법

input().split() 의 값이 문자열이 담긴 리스트므로 Output 과 같은 값을 얻으려면 map, int 함수를 사용하는 것은 바람직하지 않다. 따라서 words = input().split() 으로 바꾼다.

## 코드

```python
words = input().split()
print(words)
```

## 느낀점

<aside> 💡 새롭게 알게된 점, 어려웠던 점</aside>

없습니다.