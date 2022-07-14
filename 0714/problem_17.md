## 문제 18

> 문자열 word가 주어질 때, `**Dictionary**`를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
> 

### Input

```
banana
```

### Output

```python
b 1
a 3
n 2
```

## 접근 방법

1. collections 에서 defaultdict 를 활용했다.
2. 문제의도가 현재 진도까지만 배운 것을 활용해야할 것 같아서 한 방법이다.
3. 내가 자주 쓰는 dict 클래스의 setdefault(key, defaultvalue) 메소드를 활용한 방법이다.

## 참조

1. collections 에서 defaultdict  ↓

[https://www.daleseo.com/python-collections-defaultdict/](https://www.daleseo.com/python-collections-defaultdict/)