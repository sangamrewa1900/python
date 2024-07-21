s=0
d=11
for a in range(9,0,-1):
  for e in range(1,d-1):
   print(e,end='')
  d-=1
  for c in range(s):
   print(" ",end='')
  s+=2
  for b in range(a,0,-1):
   print(b,end='')
  print()

'''123456789987654321
12345678  87654321
1234567    7654321
123456      654321
12345        54321
1234          4321
123            321
12              21
1                1'''
