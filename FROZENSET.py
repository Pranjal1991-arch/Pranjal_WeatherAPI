nu = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# converting tuple to frozenset
fnum = frozenset(nu)
print("frozenset object is:", fnum)
nu2 = (1, 2, 6, 7)
fnum2 = frozenset(nu2)
print(fnum2.difference(fnum))
