from sets import Set
def insert(s,i):
    left = s[0:i+1]
    right = s[i+1:]
    return left + "()" + right
def genParens(rem):
    mSet = Set()
    if rem == 0:
        mSet.add('')
    else:
        prev = genParens(rem-1)
        for st in prev:
            for i in range(len(st)):
                if st[i] == '(':
                    st = insert(st,i)
                    mSet.add(st)
            mSet.add("()"+st);
    return mSet
print(genParens(3))
