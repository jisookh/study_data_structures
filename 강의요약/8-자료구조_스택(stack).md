# 자료구조 스택 (Stack)
- 삽입(push)과 삭제(pop), 탐색 연산을 제공
- 순차적으로 값이 저장되며, 가장 최근에 들어온 값부터 삭제가 됨
- 리스트도 스택과 비슷하게 사용할 수 있으나, 필요에 따라 스택을 사용하여 가능한 연산을 제한하여 데이터 사용에서 실수를 줄이고자 함
- 기타 연산자:
    * top: 가장 위의 값을 리턴 (삭제 X)
    * len: 스택에 저장된 값의 개수를 리턴
    
```python
class Stack:
    def __init__(self):
        self.items = []     # 데이터 저장을 위한 리스트 준비

    def push(self, val):        
        self.items.append(val)          # O(1)

    def pop(self):
        try:                # pop할 아이템이 없으면
            return self.items.pop()     # O(1)
        except IndexError:  # indexError 발생
            print("Stack is empy")
    
    def top(self):
        try:
            return self.items[-1]       # O(1)
        except IndexError:
            print("Stack is empty")
        
    def __len__(self):      # len()로 호출하면 stack의 item 수 반환
        return len(self.items)          # O(1)
# push, pop, top, len 모두 수행시간은 상수시간
```

## 스택 활용 예 1: 괄호 맞추기
문제: 입력은 왼쪽과 오른쪽 괄호의 문자열이 주어짐\
출력: 괄호의 쌍이 맞으면 `True`, 아니면 `False`\
해결 방법:\
문자열을 읽어, 왼쪽 괄호가 나타나면 스택에 push되어 대기하다가 오른쪽 괄호가 나타나 쌍을 이루면 스택을 pop\
최종적으로 문자열을 다 읽었을 때, 스택이 비어있으면 `True`\
스택에 남아있는 괄호가 있거나, pop을 했는데 IndexError가 발생하면 `False`

```python
def parenthesis(ParSeq):
    S = Stack()
    for p in ParSeq:
        if p == '(': S.push(p)
        elif p == ')': 
            if len(S) > 0: S.pop()
            else: return False
        else: return "Not allowed symbol"
    if len(S) > 0: return False
    else: return True
```