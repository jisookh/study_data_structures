# Big-O 표기법
알고리즘의 수행시간 = 최악의 경우의 입력에 대한 기본연산 횟수

> **알고리즘 시간복잡도 2 예제**\
Algorithm1: $T_1(n) = 2n-1$\
Algorithm2: $T_2(n) = 4n + 1$\
Algorithm3: $T_3(n) = \frac{3}{2}n^2 + \frac{3}{2}n + 1$

- Algorithm2가 Algorithm1 보다 2배 느리다
- Algorithm3은 $n<\frac{5}{3}$이면 Algorithm2 보다 빠르다
- Algorithm3은 모든 $n$에 대해서 Algorithm1 보다 느리다
- Algorithm3은 $n>\frac{5}{3}$면 항상 Algorithm2 보다 느리다
- $T_1(n)$, $T_2(n)$은 $n$에 대해 선형적으로 증가한다
    * 증가율의 관점에서 $T_1$과 $T_2$는 동일하다
- $T_3(n)$은 $n$에 대해 제곱으로 증가한다
- 수행시간을 최고차항만으로 간결하게 표기하는 것을 Big-O(대문자 O) 표기법이라고 한다
    * 최고차항만 남긴다
    * 최고차항의 계수는 생략한다
    * Big-O(최고차항)으로 표기한다\
        $T_1(n) = 2n-1 \rightarrow T_1(n) = O(n)$\
        $T_2(n) = 4n+1 \rightarrow T_2(n) = O(n)$\
        $T_3(n) = \frac{3}{2}n^2 + \frac{3}{2}n + 1 \rightarrow T_3(n)=O(n^3)$

- O최고차항은 집합으로 이해할 수 있다\
    $T_1(n) = O(n) \rightarrow T_1(n) \in O(n)$\
    $T_2(n) = O(n) \rightarrow T_2(n) \in O(n)$\
    $T_3(n) = O(n) \rightarrow T_3(n) \in O(n^2)$\
    $O(1) \subset O(n) \subset O(n^2)$

### 예제
```python
def increment_one(a):
    return a+1
```
$T(n)=1=O(1)$

```python
def number_of_bits(n):
    count = 0
    while n > 0:
        n = n//2
        count += 1
    return count
```
$n \rightarrow n/2 \rightarrow n/2^2 \rightarrow ... \rightarrow n/2^\text{count} \rightarrow 0$\
$n/2^\text{count} = 1$\
$n = 2^\text{count}$\
$\log_2{n}=\text{count}$\
$T(n)=4\log_2{n}+1=O(\log_2n)$