s=0
for a in range(9,0,-1):
 for b in range(1,a+1):
  print(b,end='')
 for c in range(s):
  print(" ",end='')
 s+=2
 for d in range(a,0,-1):
  print(d,end='')
 print()

s2=16
for f in range(1,10):
  for g in range(1,f+1):
   print(g,end='')
  for m in range(s2):
   print(" ",end='')
  s2=s2-2
  for h in range(f,0,-1):
   print(h,end='')
  print()

'''
123456789987654321
12345678  87654321
1234567    7654321
123456      654321
12345        54321
1234          4321
123            321
12              21
1                1
1                1
12              21
123            321
1234          4321
12345        54321
123456      654321
1234567    7654321
12345678  87654321
123456789987654321
'''
