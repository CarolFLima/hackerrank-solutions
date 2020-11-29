
def alternatingCharacters(s):
    previous_char = ''
    counter = 0
    total_counter = 0
    for char in s:
        if previous_char == char:
            counter += 1
        else:
            total_counter += counter
            counter = 0
            previous_char = char
    if counter > 0:
        total_counter += counter
    return total_counter


s = input()
result = alternatingCharacters(s)
print(result)