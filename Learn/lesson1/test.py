
l1 = [1,2,4,6,3,4,2,1]
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)