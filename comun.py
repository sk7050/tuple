#batch_02
#duplicate_values_in_two_tuples
'''********************************'''
x=1,'a','b',5,'z','d'
y=1,4,5,'q','d','a'
z=list()
for i in x:
  for j in y:
    if(i==j):
     z.append(i)
print("duplicate values in two tuples",tuple(z))