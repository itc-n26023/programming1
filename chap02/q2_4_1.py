#a, r1 = divmod(23,2)
#a, r2 = divmod(a,2)
#a, r3 = divmod(a,2)
#a, r4 = divmod(a,2)
#a, r5 = divmod(a,2)
#print(a)
#print(r5,r4,r3,r2,r1)
b23 = ''
a = 23 
while a != 0 : #aが0になるまで処理を繰り返す
    a, r = divmod(a,2)
    b23 = str(r) + b23
print(b23)
