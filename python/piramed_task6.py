s=16
for a in range(1,10):
   for b in range(1,a+1):
    print(b,end='')
   for c in range(s):
    print(" ",end='')
   s-=2
   for d in range(a,0,-1):
    print(d,end='')
   print()
'''
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
