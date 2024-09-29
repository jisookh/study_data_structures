# 자료구조 큐 (Queue)
- FIFO (First-In First-Out) 규칙의 순차적 자료구조

| |stack|queue|
|------|---|---|
|insert|push|enqueue|
|delete|pop|dequeue|

```python
class Queue:
    def __init(self):
        self.items = [] # 빈 리스트
        self.front_index = 0
    def enqueu(self, val):
        self.items.append(val)
    def dequeue(self):
        if self.front_index == len(self.items):
            print("Queue is empty")
        else:
            x = self.items[front_index]
            self.front_index += 1
            return x
```
## 큐 활용 예: Josephus problem
Q: n명의 사람이 원형으로 배치하고 있을 때, 1번 사람부터 숫자를 세기 시작하여 k번째 사람이 죽고, 그 다음 사람부터 다시 1번 부터 숫자를 세어 k번째 사람이 죽는다. 이 때 최후에 남게 되는 사람의 번호는?
A: 숫자 1부터 n까지 순차적으로 삽입된 queue를 준비한다. 왼쪽에서 dequeue하여 오른쪽에서 enqueu하는 것을 반복하다가 k번째에서는 dequeue만을 실행한다. 이렇게 반복하여 마지막에 남은 숫자가 생존자의 번호가 된다.

# Stack + Queue = Dequeue
- 자료의 insert와 delete가 양쪽 모두에서 가능함
- append, appendleft, pop, popleft
- python에서는 deque라는 class가 제공됨 