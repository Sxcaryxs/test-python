a=[21,8,15,3,12]
b=[10,9,12,15,18]
c=[2,3,8,9,12]
d=[4,5,6]



a.extend(b)
a.extend(c)
print(a)
a.insert(-1,20)
print(a)
a.sort(reverse=True)
print(a)
a.append(d)
print(a)


