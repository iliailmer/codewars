def balanced_parens(n):
    ret = []
    if n == 0:
        ret.append('')
    for i in range(n):
        for j in balanced_parens(i):
            for k in balanced_parens(n-i-1):
                ret.append('(' + j + ')' + k)
    return ret


print(balanced_parens(5))
