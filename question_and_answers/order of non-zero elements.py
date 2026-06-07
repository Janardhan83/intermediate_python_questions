# All non-zero elements keep their order, and all zeros move to the end.
''' method -1'''

li=[1,0,7,0,9,0]
j=0
for i in range(len(li)):
  if li[i] != 0:
    li[j],li[i]=li[i],li[j]
    j =j+1
print(li)


''' m-2'''
li=[1,0,7,0,9,0]
nz=li.count(0)
for i in li:
  if i == 0:
    li.remove(i)
print(li+[0]*nz)



''' method -3'''
li = [1, 0, 0, 0, 0, 7, 0, 9, 0]

n = len(li)   # Original length
i = 0

while i < n:
    if li[i] == 0:
        li.append(0)
        li.pop(i)
        n -= 1      # One original element processed
    else:
        i += 1

print(li)
