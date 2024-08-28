### 1. Reverse a String Using a Stack
#- **Task:** Implement a stack data structure to reverse a string

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    
def reverse_string(input_string: str) -> str:
    stack = Stack()
    for char in input_string:
        stack.push(char)
    
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str


print(reverse_string('Hello'))