
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def swap(head, k, level, traversal):
    if head is not None:
        if level%k==0:
            head.left, head.right = head.right, head.left
        
        if head.left is not None:
            swap(head.left, k, level+1, traversal)
        traversal.append(head.data)
        if head.right is not None:
            swap(head.right, k, level+1, traversal)       
            
def swapNodes(indexes, queries):
    head = Node(1)
    queue = [head]
    
    # Creating tree
    for l, r in indexes:
        temp = queue.pop(0)
        if l != -1:
            temp.left = Node(l)
            queue.append(temp.left)
        if r != -1:
            temp.right = Node(r)
            queue.append(temp.right)
      
    # Swap
    result = []
    for k in queries:
        traversal = []
        swap(head, k, 1, traversal)
        result.append(traversal)
    return result
        

if __name__ == '__main__':
    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
    print(result)
