def fun(string):
    out=str()
    for i in range(len(string)-1,-1,-1):
        out+=string[i]
    print(out)

fun("Apple")