## 문제 19. 숫자의 길이 구하기

> 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. **양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지**

### Input

```
123
```

### Output

```
3
```

## 접근 방법

10으로 나누는 것으로 자릿수를 세면 된다.

## 코드

```python
N = int(input())
count = 0

while N > 0:
    N //= 10
    count += 1
    
print(count)
```

## 느낀점

<aside> 💡 새롭게 알게된 점, 어려웠던 점</aside>

없습니다.