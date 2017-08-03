#Remove Duplicates from an unsorted Linked List
import unittest
from collections import Counter
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __str__(self):
        return str(self.data)

def remove_dup(head):
    n = head
    c = Counter()
    c[n.data] +=1
    while(n.next != None):
        c[n.next.data] +=1
        if(c[n.next.data] > 1):
           # Let garbage collection remove node
           n.next = n.next.next 
        else:
            n=n.next
    return head

def print_all(head):
    n = head 
    while(n != None):
        print(n)
        n = n.next

if __name__ == "__main__":
    n1 = Node(2)
    n2 = Node(1)
    n3 = Node(2)
    n4 = Node(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
remove_dup(n1)
print_all(n1)
