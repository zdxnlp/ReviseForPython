from collections import deque

"""普通队列"""
# deque是python提供的双端队列。append():队尾入队;popleft():队头出队;时间复杂度均为O(1),性能远高于list实现的队列
class Queue:
    def __init__(self):
        self.queue = deque() # 创建双端队列对象

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self,x):
        self.queue.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.queue.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def __str__(self):
        return f"Queue({list(self.queue)})"

"""链式队列"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None # 指向队头指针
        self.tail = None # 指向队尾指针
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self,value):
        if self.is_empty():
            node = Node(value)
            self.front = node
            self.tail = node
            self.size += 1
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        if self.size == 1:
            data = self.front.value
            self.front = None
            self.tail = None
            self.size = 0
            return data
        else:
            data = self.front.value
            self.front = self.front.next
            self.size -= 1
            return data

    def front(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.front.value

    def size(self):
        return self.size

    def __str__(self):
        result = []
        current = self.front
        while current:
            result.append(str(current.value))
            current = current.next
        return "Queue(front -> " + " -> ".join(result) + ")"

"""循环队列"""

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q)
    print(q.front())
    print(q.dequeue())
    print(q)

    lq = LinkedQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    print(lq)
    print(lq.dequeue())
    print(lq)