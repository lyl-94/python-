def tostring(param):
    res = ''
    for i in range(len(param)):
        if i == 0:
            res += str(param[i])
        elif i == len(param)-1:
            res += ', and ' + str(param[i])
        else:
            res += ', ' + str(param[i])
    return res


print(tostring(['apple', 'pie', 0, 1]))
