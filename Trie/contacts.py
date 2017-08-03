class Node:
    def __init__(self, char=None):
        self.char = char
        self.children = []
        self.end = False
        self.word_amt = 0
        
    def get_child(self,c):
        for child in self.children:
            if child.char == c:
                return child
        return None

class Trie:
    def __init__(self):
        self.head = Node("*")
    
    def add(self, word):
        current_node = self.head
        for c in word:
            next_node = current_node.get_child(c)
            if next_node is None:
                next_node = Node(c)
                current_node.children.append(next_node)
            next_node.word_amt += 1
            current_node = next_node
        current_node.end = True 
        
    def search(self, prefix):
        """ Returns a list of all words in tree that start with prefix """
        curr = self.head
        for c in prefix:
            next_node = curr.get_child(c)
            if next_node is None:
                return 0
            curr = next_node
        return curr.word_amt
n = int(input().strip())
trie = Trie()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        trie.add(contact) 
    else:
        print(trie.search(contact))
