def decodeHuff(root, s):
    result = ''
    node = root
    for c in s:
        if c == '0':
            node = node.left
        else: 
            node = node.right
        
        if node.left is None and node.right is None:
            result += node.data
            node = root
    print(result)
