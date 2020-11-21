from collections import Counter

def checkMagazine(magazine, note):
    if not (Counter(note)-Counter(magazine)):
        print("Yes")
    else:
        print("No")
