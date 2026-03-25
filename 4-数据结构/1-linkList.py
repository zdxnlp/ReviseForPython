# 定义链表的节点
class Node:
    def __init__(self,data):
        self.data = data # 节点数据
        self.next = None # 指向下一个节点的指针，初始为None

class SinglyLinkedList:
    def __init__(self):
        self.head = None # 头节点（初始为空）head之后要存引用
        self._size = 0 # 链表长度（优化获取长度的时间复杂度）

    # 获取链表长度
    def __len__(self):
        return self._size

    # 判空
    def is_empty(self):
        return self._size == 0

    # 在末尾插入新节点
    def append(self,data):
        new_node = Node(data) # 创建一个新的节点
        if self.is_empty():
            self.head = new_node # head等于新节点的引用，也就是存的是新节点的地址，也就只想了心结点
        else:
            current = self.head # 创建一个动态“指针”
            while current.next : # 遍历到最后一个节点
                current = current.next
            current.next = new_node # 将节点插入到链表末尾
        self._size += 1

    # 在index所指的位置插入新节点(默认链表第一个元素是0号元素)
    def insert(self,index,data):
        if index > self._size or index < 0:
            raise IndexError("index out of range")
        new_node = Node(data) # 创建新节点,这里就已经将data值写入了心结点了，之后就只需要进行指针的修改，并且创建节点的时候，它的next就默认为None
        if index == 0: # 在头部插入
            new_node.next = self.head # 新节点的next改为原来的头节点
            self.head = new_node # 头节点指向更改
        else:
            current = self.head # 利用current指针遍历到要插入的位置
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self._size += 1

    # 删除指定索引处的节点，并返回删除的数据
    def remove(self,index):
        if index >= self._size or index < 0 or index == 0:
            raise IndexError("index out of range/remove from empty list")
        if index == 0: # 删除头部
            data = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            data = current.next.data
            current.next = current.next.next
        self._size -= 1
        return data

    # 获取制定索引处的节点数据
    def get(self,index):
        if index >= self._size or index < 0:
            raise IndexError("index out of range")
        if self.is_empty():
            raise IndexError("list is empty")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    # 支持print()打印链表
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)

if __name__ == '__main__':
    linked_list = SinglyLinkedList() # 初始化链表
    #print(linked_list)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)
    print(linked_list)
    linked_list.insert(0,7)
    print(linked_list)
    a = linked_list.remove(3)
    print(a)
    print(linked_list)
