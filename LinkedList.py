class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        if(self.head is None):
            self.insertAtBeginning(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        print(count)

    def insertAtIndex(self, index, data):
        prevNode = self.head
        for i in range(index-1):
            prevNode = prevNode.next

        prevNode.next = Node(data, prevNode.next)

    def removeAtFirst(self):
        if(self.head is None):
            print("LL is empty")
            return
        self.head = self.head.next

    def removeAtLast(self):
        if (self.head is None):
            print("LL is empty")
            return

        prevNode = self.head
        while prevNode.next.next:
            prevNode = prevNode.next

        prevNode.next = None

    def removeAtIndex(self, index):
        if(self.head is None):
            print("LL is empty")
            return

        if(index == 0):
            self.removeAtFirst()

        prevNode = self.head
        for i in range(index - 1):
            prevNode = prevNode.next

        prevNode.next = prevNode.next.next




    def print(self):
        if (self.head is None):
            print("LL is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def reversePrint(self):
        if (self.head is None):
            print("LL is empty")
            return

        itr = self.head
        llstr = []
        while itr:
            llstr.append(itr.data)
            itr = itr.next
        llstr = llstr[::-1

                ]
        for i in llstr:
            print(i, "-->", end="")



if __name__ == '__main__':
    ll = Linkedlist()
    ll.insertAtBeginning(10)
    ll.insertAtBeginning(20)
    # ll.print()
    ll.insertAtEnd(30)
    ll.insertAtEnd(40)
    # ll.print()
    # ll.length()
    ll.insertAtIndex(2, 100)
    ll.print()
    ll.removeAtFirst()
    ll.print()
    # ll.removeAtLast()
    # ll.print()
    ll.removeAtIndex(1)
    ll.print()
    ll.reversePrint()
