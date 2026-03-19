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

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = None # 头指针
        self.size = 0 # 栈的元素个数

    # 判断是否为空
    def is_empty(self):
        return self.size == 0

    # 头插法实现
    def push(self,data):
        node = Node(data) # 创建新的节点，并将data填入新节点中
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.head.data

    def size(self):
        return self.size

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return "Stack(top -> " + " -> ".join(result) + ")"


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

    ls = LinkedStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    ls.push(4)
    print(ls)