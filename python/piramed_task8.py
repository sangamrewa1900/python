sp=8
for a in range(1,9):
   for c in range(sp):
     print(" ",end='')
   sp=sp-1
   for b in range(1,a+1):
     print(b,end='')
   for d in range(a-1,0,-1):
     print(d,end='')
   print()

spc=2
for s in range(7,0,-1):
   for t in range(spc):
     print(" ",end='')
   spc=spc+1
   for u in range(1,s+1):
     print(u,end='')
   for v in range(s-1,0,-1):
     print(v,end='')
   print()
'''
        1
       121
      12321
     1234321
    123454321
   12345654321
  1234567654321
 123456787654321
  1234567654321
   12345654321
    123454321
     1234321
      12321
       121
        1
'''
