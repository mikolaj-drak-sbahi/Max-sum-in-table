def NSBSS(t):
    s = [t[0],max(t[0],t[1])]

    for i in range(2, len(t)):
        if t[i] + s[i - 2] > s[i - 1]:
            s.append(t[i] + s[i - 2])
        else:
            s.append(s[i - 1])
    return s



def NSBSS2(t):
    s = [[], []]
    s[0].append([t[0][0]])
    s[0].append([t[0][1]])
    s[0].append([])

    s[1].append([t[1][0]] + s[0][1])
    s[1].append([t[1][1]] + s[0][0])
    s[1].append(max(s[0][0], s[0][1], key=sum))
    for i in range(2, len(t)):
        if sum(s[i - 1][1]) > sum(s[i - 1][2]):
            lewa = [t[i][0]] + s[i - 1][1]
        else:
            lewa = [t[i][0]] + s[i - 1][2]

        if sum(s[i - 1][0]) > sum(s[i - 1][2]):
            prawa = [t[i][1]] + s[i - 1][0]
        else:
            prawa = [t[i][1]] + s[i - 1][2]
        nic = max(s[i - 1][0], s[i - 1][1], key=sum)
        s.append([lewa, prawa, nic])

    max_sum = max(s[-1], key=sum)
    return s, max_sum, sum(max_sum)


tab1 = [[5, 2], [100, 5], [2, 5], [23, 150]]
tab11 = [[1, 2], [1, 5], [2, 5], [23, 150], [1, 250]]  
tab = [[5, 2], [2, 5], [2, 100]]
print("Lista wyników pośrednich: ", NSBSS2(tab)[0])
print("Podzbiór o największej sumie: ", NSBSS2(tab)[1])
print("Największa suma: ", NSBSS2(tab)[2])

