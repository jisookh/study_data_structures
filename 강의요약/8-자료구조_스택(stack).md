# Stack
- 삽입(push)과 삭제(pop), 탐색 연산은 모든 자료구조에서 제공되어야함
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
        self.items.append(val)

    def pop(self):
        try:                # pop할 아이템이 없으면
            return self.items.pop()
        except IndexError:  # indexError 발생
            print("Stack is empy")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
        
    def __len__(self):      # len()로 호출하면 stack의 item 수 반환
        return len(self.items)
```