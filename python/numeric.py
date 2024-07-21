'''
if value is numeric and grater then 10.then pint value
'''
l=["sangam",20,"rishr",45,47,"san","des","sde",458,10,9,"sanam"]
for a in l:
    if str(a).isnumeric() and a>=10:
        print(a)
