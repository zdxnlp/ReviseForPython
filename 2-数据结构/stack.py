class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'Stack{self.items}'

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    peak = s.peek()
    print(peak)
    top = s.pop()
    print(top)
    print(s)