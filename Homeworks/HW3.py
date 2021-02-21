def prime_first(val):
  primes=[]
  for i in range(val,val+1):
    if i > 1:
      for j in range(2,i):
        if (i % j) == 0:
          break
      else:
        print(i)

def prime_second(val):
  primes=[]
  for i in range(val,val+1):
    if i > 1:
      for j in range(2,i):
        if (i % j) == 0:
          break
      else:
        print(i)

for x in range(1000):
    if x<500:
      prime_first(x)
    else :
      prime_second(x)
