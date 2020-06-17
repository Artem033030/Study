
# print([x for x in range(1,1000,5)])
# print([x*x*x for x in range(1,50,3) if x % 2 == 0])
print([x*x*x if x % 2 == 0 else -1 for x in range(1,50,3) ])
print([for x in range(1,1000000,7)if x % 7 == 0]  )












# a = []
# for x in range(1,100,5):
#     a.append(x)

a = []
for x in range(1,50,1):
    if x % 2 == 0:
        a.append(x*x*x)
    else:
        a.append(-1)
print(a)
