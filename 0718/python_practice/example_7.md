## 예제 07. [오류 해결] 평균 구하기

> 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

### 오류 코드

```python
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1

print(total // count)
```

### Ouput

```
5.5
```

## 접근 방법

해당 코드는 number_list 가 참조하고 있는 리스트의 총합 / 개수 를 구하는거 같다. 그러면 count 부분이 들여쓰기가 있어야한다.

실수가 출력값이므로 // 가 아닌 / 연산자를 사용한다.

## 코드

```python
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
	count += 1

print(total / count)
```

## 느낀점

<aside> 💡 새롭게 알게된 점, 어려웠던 점</aside>

없습니다.