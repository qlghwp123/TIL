## 문제 21.

> 주어진 숫자를 뒤집은 결과를 출력하시오. 
> <span style="color:red">  * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지</span>

### Input

```python
1234
```

### Output

```
4321
```

## 접근 방법

1. 입력값이 들어오면 복사본을 떠서 그것을 0이 될 때가지 나눔과 동시에 계속해서 1씩 더한다. 

2. 그렇게 자릿수가 구해지면 다시 입력값의 복사본을 구한다.

3. 아까 구한 자릿수가 0 이 될 때까지 1씩 감소시킨다.
4. 복사본을 10으로 나눈 나머지에 10의 (현재 자릿수 - 1) 만큼 거듭제곱수를 곱해서 result 에 계속 합산시킨다.

## 코드

```python
number = int(input())

cp = number
length = 0

while cp != 0:
    length += 1
    cp //= 10

cp = number
result = 0

while length > 0:
    result += (cp % 10) * (10 ** (length - 1))
    cp //= 10
    length -= 1 

print(result)
```

## 느낀점

<aside>
💡 새롭게 알게된 점, 어려웠던 점
</aside>

없습니다.