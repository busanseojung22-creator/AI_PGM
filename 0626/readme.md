````markdown
# Python 컨테이너(Container) 정리

## 1. 컨테이너(Container)란?

컨테이너(Container)는 **여러 개의 데이터를 하나로 묶어서 저장하는 자료형**입니다.

예를 들어 학생 5명의 점수를 저장한다고 하면

```python
score1 = 90
score2 = 85
score3 = 78
score4 = 95
score5 = 88
```

이렇게 각각 저장할 수도 있지만,

컨테이너를 사용하면

```python
scores = [90, 85, 78, 95, 88]
```

처럼 하나의 변수에 여러 개의 데이터를 저장할 수 있습니다.

---

# 2. Python의 대표적인 컨테이너

| 자료형 | 특징 | 기호 |
|---------|------|------|
| List | 순서 O, 수정 O | [] |
| Tuple | 순서 O, 수정 X | () |
| Dictionary | Key-Value 저장 | {} |
| Set | 중복 X, 순서 X | {} |

---

# 3. List (리스트)

가장 많이 사용하는 컨테이너

## 생성

```python
numbers = [10, 20, 30]
```

문자열도 저장 가능

```python
fruits = ["apple", "banana", "orange"]
```

혼합도 가능

```python
data = [10, "apple", True]
```

---

## 요소 접근

```python
numbers = [10,20,30]

print(numbers[0])
print(numbers[1])
print(numbers[2])
```

출력

```
10
20
30
```

마지막 요소

```python
print(numbers[-1])
```

---

## 주요 함수

```python
numbers.append(40)
```

마지막 추가

```python
numbers.remove(20)
```

값 삭제

```python
numbers.pop()
```

마지막 요소 삭제

```python
len(numbers)
```

길이

```python
sum(numbers)
```

합

```python
max(numbers)
```

최대값

```python
min(numbers)
```

최소값

---

# 4. Tuple (튜플)

리스트와 거의 같지만

**수정이 불가능한 컨테이너**

생성

```python
numbers = (10,20,30)
```

접근

```python
print(numbers[0])
```

가능

수정

```python
numbers[0] = 100
```

오류 발생

```
TypeError
```

---

## 언제 사용하는가?

변경되면 안 되는 데이터

예)

```python
days = (
    "월",
    "화",
    "수",
    "목",
    "금",
    "토",
    "일"
)
```

좌표

```python
point = (100,200)
```

RGB

```python
color = (255,0,0)
```

---

# 5. Dictionary (딕셔너리)

Key와 Value를 저장

생성

```python
fruit = {
    "apple":"사과",
    "banana":"바나나"
}
```

값 가져오기

```python
print(fruit["apple"])
```

출력

```
사과
```

숫자도 Key 가능

```python
data = {
    1:"apple",
    2:"banana"
}
```

---

## 값 추가

```python
fruit["orange"] = "오렌지"
```

---

## 값 수정

```python
fruit["apple"] = "사과(수정)"
```

---

## 값 삭제

```python
del fruit["banana"]
```

---

## 주요 함수

```python
fruit.keys()
```

Key 목록

```python
fruit.values()
```

Value 목록

```python
fruit.items()
```

Key, Value 함께

---

# 6. Set (집합)

중복을 허용하지 않는 컨테이너

```python
numbers = {1,2,3,3,4,4}
```

출력

```
{1,2,3,4}
```

자동으로 중복 제거

---

## 요소 추가

```python
numbers.add(5)
```

---

## 요소 삭제

```python
numbers.remove(2)
```

---

## 집합 연산

합집합

```python
a | b
```

교집합

```python
a & b
```

차집합

```python
a - b
```

---

# 7. list(), tuple(), set(), dict()

자료형 변환

리스트

```python
list("apple")
```

결과

```python
['a','p','p','l','e']
```

튜플

```python
tuple([1,2,3])
```

결과

```
(1,2,3)
```

집합

```python
set([1,2,2,3])
```

결과

```
{1,2,3}
```

---

# 8. 컨테이너 비교

| 항목 | List | Tuple | Dictionary | Set |
|------|------|--------|------------|------|
| 순서 유지 | O | O | O(Python 3.7+) | X |
| 수정 가능 | O | X | O | O |
| 중복 허용 | O | O | Key X | X |
| 인덱스 사용 | O | O | X | X |

---

# 9. 언제 무엇을 사용할까?

### List

- 데이터를 자주 수정한다.
- 순서가 중요하다.

예)

```python
students = ["Tom","Jane","Mike"]
```

---

### Tuple

- 절대 변경되지 않는다.

예)

```python
point = (100,200)
```

---

### Dictionary

- 이름으로 값을 찾고 싶다.

예)

```python
student = {
    "name":"Tom",
    "age":20
}
```

---

### Set

- 중복 제거
- 집합 계산

예)

```python
numbers = {1,2,3,3,4}
```

---

# 10. 자주 사용하는 내장 함수

```python
len(container)
```

길이

```python
sum(numbers)
```

합

```python
max(numbers)
```

최대값

```python
min(numbers)
```

최소값

```python
type(data)
```

자료형 확인

예)

```python
print(type([1,2,3]))
```

출력

```
<class 'list'>
```

---

# 11. 초보자가 자주 하는 실수

❌ `dict`, `list`, `set`, `tuple`를 변수명으로 사용

```python
dict = {}
list = []
```

가능은 하지만 권장하지 않습니다.

대신

```python
fruit_dict = {}
numbers = []
```

처럼 의미 있는 이름을 사용하세요.

---

# 12. 핵심 요약

| 자료형 | 기억할 핵심 |
|---------|-------------|
| List | 가장 많이 사용, 수정 가능 |
| Tuple | 수정 불가능 |
| Dictionary | Key로 Value를 찾는다. |
| Set | 중복 제거, 집합 연산 |

---

# 한 줄 암기

- **List** → 순서 O, 수정 O
- **Tuple** → 순서 O, 수정 X
- **Dictionary** → Key : Value
- **Set** → 중복 X
````

