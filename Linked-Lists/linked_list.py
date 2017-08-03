def Insert(head, data):
    if(head==None):
        head = Node(data)
    else:
        runner = head
        while(runner.next != None):
            runner=runner.next
        runner.next = Node(data)
    return head
j
def Delete(head, pos):
    if(pos == 0):
        temp = head.next
        del head
        return temp
    else:
        runner = head
        while(pos-1>0):
            runner = runner.next
            pos -=1
        runner.next = runner.next.next
        return head

def ReversePrint(head):
    if(head):
        ReversePrint(head.next)
        print(head.data)

def Print(head)
	if(head):
		print(head.data)
		Print(head)
		
def MergeLists(headA, headB):
    if(headA == None and headB == None):
        return None
    elif(headA==None and headB):
        return headB
    elif(headA and headB == None):
        return headA
    if(headA.data < headB.data):
        headA.next = MergeLists(headA.next,headB)
    elif(headA.data > headB.data):
        temp = headB
        headB = headB.next
        temp.next = headA
        headA = temp
        headA.next = MergeLists(headA.next,headB)
    return headA
