n =int(input())
i = 0
fibo=[]
while i < n:
    if i == 0 or i == 1:
        fibo.append(i)
     
    if i > 1:
        aux = fibo[i-2] + fibo[i-1]
      
        fibo.append(aux)
    i = i + 1
for j in range(0, n):
    fibo[j] =str(fibo[j])
  
fibo = ' '.join(fibo)
print(fibo)
