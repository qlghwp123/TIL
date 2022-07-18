## 예제 10. [오류 해결] 더 큰 최댓값 찾기

> 아래 코드는 리스트에서 최댓값을 구하는 코드입니다. 코드에서 오류를 찾아 원인을 적고, 수정하세요.

### 오류 코드

```python
number_list = [1, 23, 9, 6, 91, 59, 29]
max = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
```

### Output

```
두 번째 리스트의 최댓값이 더 큽니다.
```

## 접근 방법

max 라는 것은 파이썬에서 내장함수로 사용하고 있는 예약어로써, 현재 코드에서 문법 오류를 일으킨다. 따라서 max 가 아닌 max1 이나 다른 변수 명으로 바꿔야한다.

## 코드

```python
number_list = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
```

## 느낀점

<aside> 💡 새롭게 알게된 점, 어려웠던 점</aside>

없습니다.