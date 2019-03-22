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
    def length(self,headNode):
        if headNode is None:
            return 0
        else:
            return 1+self.length(headNode.next)
    def swap(self,val,val1):
        if(val==val1): # case 1: same node
            print("Same node.")
        prev = None # case 2: swap with head
        curNode = self.head
        while curNode != None and curNode.data != val:
            prev = curNode
            curNode = curNode.next
        prev1 = None # case 3: swap nodes
        curNode1 = self.head
        while curNode1 != None and curNode1.data != val1:
            prev1 = curNode1
            curNode1 = curNode1.next
        if curNode == None or curNode == None: # case 4: invalid input for one of the node values
            print("At least one of the nodes doesn't exist")
        else:
            if prev == None:
                self.head = curNode1
                prev1.next = curNode
            elif prev1 == None:
                self.head = curNode
                prev.next = curNode1
            else:
                prev.next = curNode1
                prev1.next = curNode
            temp = curNode.next
            temp1 = curNode1.next
            curNode.next= temp1
            curNode1.next = temp
    def reverse(self):
        prev = None
        curNode = self.head
        while curNode != None: # iterate through linked list
            temp = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = temp
        self.head = prev # last iteration so last node will equal the head
    def printList(self):
        curNode = self.head
        while curNode != None: # changed from curNode.next to curNode and it works correctly
            print(curNode.data)
            curNode = curNode.next
        print("")
        
link = linkedList() # instantiate linked list object
link.append(5) # pop
link.printList()
link.append(6) # pop
link.printList()
link.prepend(7) # pop back
link.printList()
link.insertAfter(link.head,8) # pop after head
link.printList()
link.deleteNode(5) # delete 5 node
link.printList() 
link.swap(7,6) # swap 7 and 6 nodes
link.printList()
link.reverse()
link.printList()