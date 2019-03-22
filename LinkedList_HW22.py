#
# Sam Ghalayini
# HW 22 Singly Linked Lists
#
# CLASS NOTES + Homework
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            lastNode = self.head 
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = newNode
    def prepend(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
    def insertAfter(self,prevNode,data):
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
    def deleteNode(self,key):
        curNode = self.head
        if curNode != None and curNode.data ==key:
            self.head =curNode.next
            curNode = Node
            return
        else:
            prevNode = None
            while curNode != None and curNode.data != key:
                prevNode = curNode
                curNode = curNode.next
            if curNode == None:
                print("Error cannot delete node")
            else:
                prevNode.next = curNode.next
                curNode = None
    def printList(self):
        curNode = self.head
        while curNode != None: # changed from curNode.next to curNode and it works correctly
            print(curNode.data)
            curNode = curNode.next
        print("")

link = linkedList()
link.append(5)
link.printList()
link.append(6)
link.printList()
link.prepend(7)
link.printList()
link.insertAfter(link.head,8) # link.head will return 8 right after the first number, then every next will move it one more, error if there are too many ".next"'s
link.printList()
link.deleteNode(5)
link.printList() 

