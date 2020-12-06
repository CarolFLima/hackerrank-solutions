
def triplets(a, b, c):

    total = 0
    a_list = sorted(list(set(a)))
    b_list = sorted(list(set(b)))
    c_list = sorted(list(set(c)))

    a_qtd = 0
    c_qtd = 0
    for b_value in b_list:
        while a_qtd<len(a_list) and a_list[a_qtd] <= b_value:
            a_qtd += 1

        while c_qtd<len(c_list) and c_list[c_qtd] <= b_value:
            c_qtd += 1
        
        total += a_qtd*c_qtd
    return total


lenaLenbLenc = input().split()

lena = int(lenaLenbLenc[0])

lenb = int(lenaLenbLenc[1])

lenc = int(lenaLenbLenc[2])

arra = list(map(int, input().rstrip().split()))

arrb = list(map(int, input().rstrip().split()))

arrc = list(map(int, input().rstrip().split()))

ans = triplets(arra, arrb, arrc)

