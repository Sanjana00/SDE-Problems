target = int(input())
arr = [int(x) for x in input().split()]
xor = 0
c = 0
xors = {arr[0] : 1}
if arr[0] == target:
    c += 1
for i, ele in enumerate(arr):
    if i == 0:
        continue
    xor ^= ele
    if xor == target:
        c += 1
    y = xor ^ target
    if y in xors:
        c += xors[y]
    xors[xor] = xors.get(xor, 0) + 1
print(c)

'''
Visualisation: Y ^ X = K => Y = X ^ K

'''
