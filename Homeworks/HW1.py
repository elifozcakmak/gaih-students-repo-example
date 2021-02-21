import random
primes=[]

for i in range(1,100):
  if i > 1:
    for j in range(2,i):
      if (i % j) == 0:
        break
    else:
        primes.append(i)

row=range(3)
matrix=[]
for i in range(3):
  row=[]
  for j in range(3):
    row.append(random.choice(primes))
  matrix.append(row)
  print(matrix[i])
