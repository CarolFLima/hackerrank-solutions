from collections import Counter

def checkMagazine(magazine, note):
    if not (Counter(note)-Counter(magazine)):
        print("Yes")
    else:
        print("No")

      
checkMagazine('two times three is not four', 'two times two is four')
