class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next ,self.prev = None, None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int: #Loops and goes on to the value returns none if list empty


        if index >= self.size:
            return -1

        elif index < self.size:
            curr = self.head
            for i in range(index):
                if curr.next:
                    curr = curr.next

            return curr.val

        
            

    def addAtHead(self, val: int) -> None:  
        #Different cases: No Node, addAtHead used, addAtTail used, addAtIndex used

        newNode = ListNode(val)

        if self.size == 0:
            self.head = self.tail = newNode
            
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        self.size += 1


    def addAtTail(self, val: int) -> None:
        #Different cases: No Node, addAtHead used, addAtTail used, addAtIndex used
        
        newNode = ListNode(val)

        if self.size == 0:
            self.head = self.tail = newNode
            
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        #Different cases: no node, 0th index, -1th index, ith index

        
        newNode = ListNode(val)
        if index <= self.size:
            if self.size == 0:
                self.head = self.tail = newNode
                self.size += 1


            elif index == 0 and self.size != 0:
                self.addAtHead(val)

            elif index == self.size and self.size != 0:
                self.addAtTail(val)

            else:
                curr = self.head
                for i in range(index):
                    if curr.next:
                        curr = curr.next
                ogPrev = curr.prev
                ogPrev.next, curr.prev = newNode, newNode
                newNode.prev, newNode.next = ogPrev, curr

                self.size += 1


    def deleteAtIndex(self, index: int) -> None:

        if index < self.size:
            curr = self.head
            for i in range(index):
                curr = curr.next

            if self.size == 1:
                self.head = self.tail = None

            else:
                curr = self.head

                for i in range(index):
                    curr = curr.next

                if curr.prev and curr.next:
                    ogPrev, ogNext = curr.prev, curr.next
                    ogPrev.next, ogNext.prev = ogNext, ogPrev
                    curr.next, curr.prev = None, None

                elif curr.prev and not curr.next:
                    ogPrev, ogNext = curr.prev, curr.next
                    ogPrev.next = ogNext
                    curr.prev = None
                    self.tail = ogPrev

                elif curr.next and not curr.prev:
                    ogPrev, ogNext = curr.prev, curr.next
                    ogNext.prev = curr
                    curr.next = None
                    self.head = ogNext

            self.size -= 1



# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)
