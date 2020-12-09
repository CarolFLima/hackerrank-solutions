
# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for char in s:
        if char == '{' or char == '[' or char == '(':
            stack.append(char)
        elif char == '}' or char == ']' or char == ')': 
            if len(stack) == 0:
                return 'NO'
            elif char == '}':
                if stack.pop() != '{':
                    return 'NO'
            elif char == ')':
                if stack.pop() != '(':
                    return 'NO'
            elif char == ']':
                if stack.pop() != '[':
                    return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        s = input()

        print(isBalanced(s))

    