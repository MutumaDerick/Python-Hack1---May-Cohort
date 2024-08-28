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


### 2. Implement a Queue Using Two Stacks

class QueueWithStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int):
        self.stack_in.append(x)

    def dequeue(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

# Example Usage
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue()) 
print(q.dequeue()) 

## 3: Find the Maximum element in a list using a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
            new_node = Node(value)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

    def max(self) -> int:
            if not self.head:
               raise ValueError('List is empty')
            
            max_value = self.head.value
            current = self.head.next

            while current:
                if current.value > max_value:
                    max_value = current.value
                current = current.next

            return max_value
    
# Example Usage
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.max())
