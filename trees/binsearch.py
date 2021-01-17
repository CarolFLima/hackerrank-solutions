def checkBST(root):
    return check(root, -10000000, 10000000)

    
def check(root, min, max):
    if root is None:
        return True
    return min < root.data and root.data < max and check(root.left, min, root.data) and check(root.right, root.data, max)