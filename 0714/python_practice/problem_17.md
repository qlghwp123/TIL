## 문제 17

> 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
`**.upper()`, `.swapcase()` 사용 금지**
> 

### Input

```
banana
```

### Output

```python
BANANA
```

## 추가 정보

아스키코드는 영문 알파벳을 사용하는 대표적인 문자 인코딩이고, 이후 아스키 기반의 확장 인코딩(유니코드 등)이 등장하게 되었다. 

[ASCII - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/ASCII)

[유니코드 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c8becbe8-9922-4fac-b3ef-2fbeb0f8b209/Untitled.png)

### 파이썬 활용

특정 문자에 대응 되는 유니코드 숫자로 반환하는 함수는 `ord` 이다.

[https://docs.python.org/ko/3/library/functions.html#ord](https://docs.python.org/ko/3/library/functions.html#ord)

```python
ord('a') 
# 97
```

해당 유니코드 숫자를 문자로 반환하는 함수는 `chr`이다. 

[https://docs.python.org/ko/3/library/functions.html#chr](https://docs.python.org/ko/3/library/functions.html#chr)

```python
chr(97)
# 'a'
```

## 접근 방법

반복문 써서 순회하여 아스키코드 값 가져와서 대문자로 만들고 리스트에 넣어서 다 끝나면 “”.join 으로 해당 리스트를 join 메소드 인자로 넣어 출력한다.