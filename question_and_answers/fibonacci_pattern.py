''' give input = 6 
 expected out put :-

1 
2 1 
3 5 8 
55 34 21 13 
89 144 233 377 610 
10946 6765 4181 2584 1597 987  '''

a=1
b=0
for num in range(6):
  li=[]
  if num % 2 == 0:
    for rot in range(num+1):
      print(a , end=' ')
      a , b = a+b , a
  else:
    for rot in range(num+1):
      li.append(a)
      a , b = a+b , a
    for rev in li[::-1]:
      print(rev,end=' ')
  print()

