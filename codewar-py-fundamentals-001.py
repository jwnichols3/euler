def openOrSenior(data):
    retlist = []

    for a in data:
        age = a[0]
        handicap = a[1]
        if age >= 55:
            if handicap > 7:
                retlist.append("Senior")
            else:
                retlist.append("Open")
        else:
            retlist.append("Open")
    
    return retlist

results1 = openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]])

print("Run 1:", results1)

results2 = openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]])

print("Run 2:", results2)
