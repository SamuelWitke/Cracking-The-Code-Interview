# Delete Middle Node 
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __str__(self):
        return str(self.data)

def print_all(head):
    n = head 
    while(n != None):
        print(n)
        n = n.next
def remove_mid(n):
    nextN = n.next
    n.data = nextN.data
    n.next = nextN.next

        
if __name__ == "__main__":
    n1 = Node('a')
    n2 = Node('b')
    n3 = Node('c')
    n4 = Node('d')
    n5 = Node('e')
    n6 = Node('f')
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    remove_mid(n1)
    print_all(n1)
