class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val


    def addAtHead(self, val: int) -> None:
        self.size += 1
        if not self.head:
            self.head = ListNode(val)
            return

        new_item = ListNode(val)
        new_item.next = self.head
        self.head = new_item

    def addAtTail(self, val: int) -> None:
        self.size += 1
        if not self.head:
            self.head = ListNode(val)
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
            return

        temp = self.head
        for i in range(index-1):
            temp = temp.next

        next_node = temp.next
        new_node = ListNode(val)
        temp.next = new_node
        new_node.next = next_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        
        if not temp.next:
            return
        
        temp.next = temp.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)