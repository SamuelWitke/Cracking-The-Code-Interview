#Partition Linked List
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __str__(self):
        return str(self.data)


def partition(node,piv):
    head = tail = node
    while node:
        nextN = node.next
        if(node.data < piv):
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = nextN
    tail.next= None
    return head

def reverse(head):
    prev = None
    curr = head
    nextN = None
    while(curr != None):
        nextN = curr.next
        if nextN != None: print("nextN",nextN.data)
        curr.next = prev
        if curr.next != None: print("Curr.next",curr.next.data) 
        prev= curr
        print("prev",prev.data)
        curr = nextN
        if curr != None: print("Curr",curr.data)

def print_all(head):
    n = head 
    while(n != None):
        print(n)
        n = n.next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4

reverse(n1)
#print_all(n1)
#n1=partition(n1,5)
#print_all(n1)
