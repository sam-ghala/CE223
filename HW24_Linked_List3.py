#
# Sam Ghalayini
# HW 24 Singly Linked Lists
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
    def length(self):
        count = 0
        curNode = self.head
        while curNode != None:
            curNode = curNode.next
            count += 1
        return count
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
    def deletePos(self,pos):
        curNode = self.head
        if pos == 0:
            self.head = curNode.nextcurNode = None
            return
        else:
            count = 0
            prev = None
            while curNode != None and count != pos:
                prev = curNode
                curNode = curNode.next
                count+=1
            if curNode == None:
                print("Node doesn't exist")
                return
            else:
                prev.next = curNode.next
                curNode = None
    def remov_dup(self):
        prev = None
        curNode = self.head
        data = dict()
        while curNode != None:
            if curNode.data not in data:
                data[curNode.data] = 1
                prev = curNode
                curNode = curNode.next
            else:
                prev.next = curNode.next
                curNode = None
            curNode = prev.next
    def nth_from_last(self,n): # bug fixed
        leng = self.length()
        dist = leng-1
        curNode = self.head
        while curNode != None:
            if dist == n-1:
                print(curNode.data)
                return curNode
            else:
                dist-=1
                curNode = curNode.next
    def occurs(self,data):
        count=0
        curNode = self.head
        while curNode != None:
            if curNode.data == data:
                count += 1
            curNode = curNode.next
        return count
    def rotate(self,k):
        p = self.head
        q = self.head
        prev= None
        count = 0
        while p!=None and count < k:
            prev = p
            p = p.next
            count += 1
        p = prev
        while q != None:
            prev = q
            q = q.next
        q = prev
        self.head = q.next
        p.next = self.head
        q.next = None
    def swap_tail_head(self):
        last = self.head
        nextLast = None
        while last.next != None: 
            nextLast = last
            last = last.next
        last.next = self.head
        self.head = nextLast.next
        nextLast.next = None
    def printList(self):
        curNode = self.head
        while curNode != None: # changed from curNode.next to curNode and it works correctly
            print(curNode.data)
            curNode = curNode.next
        print("")

link = linkedList() # instantiate linked list object
link.append(1) # pop
link.append(2)
link.append(3)
link.append(4)
link.append(5)
link.append(5)
link.printList()
link.remov_dup()
link.printList()
link.nth_from_last(2) # bug fixed
print("")
link.append(5)
link.append(5)
link.printList()
print("")
print(link.occurs(5))
print("")
link.swap_tail_head()
link.printList()
print("Rotate:")
link.rotate(2)
link.printList()




























