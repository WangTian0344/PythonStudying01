# 迭代器

a = [x for x in range(6)]
print(a)

for i,n in enumerate(a):
    print("i:n:{}:{}".format(i,n))

i = a.__iter__()
while i:
    print(i.__next__())