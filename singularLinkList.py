class Node:
    def __init__(self,data):
        self.data = data
        
        self.next = None
def count(head):
    current = head
    count = 1
    while current.next is not None:
        current = current.next
        count+=1
    return count
nodeA = Node(2)
nodeB = Node(5) 
nodeC = Node(3)
nodeD = Node(1)

nodeA.next= nodeB
nodeB.next= nodeC
nodeC.next = nodeD
print(count(nodeA))

        