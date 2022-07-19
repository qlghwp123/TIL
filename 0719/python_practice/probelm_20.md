## 문제 20. 각 자릿수의 합 구하기

> 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. ****
> 

### Input

```
123
```

### Output

```
6
```

## 접근 방법

입력값이 0 이 될 때까지 10으로 나눈 나머지를 계속 구해서 그것들을 모두 합산함.

## 코드

```python
number = int(input())

result = 0

while number != 0:
    result += number % 10
    number //= 10

print(result)
```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점
</aside>

없습니다.