
"""
i=0
j=0
t=0
sum1=0
sum2=0
sum3=0

while i<1000:
    if (i%3==0 ):
        sum11 +=i
    i+=1

while j<1000:
    if (j%5== 0):
        sum2 += j
    j+=1

while t<=1000:
    if (t%15== 0):
        sum3 += t
    t+=1

print("sum",sum2)
print("sum ={}".format(sum1+sum2-sum3))


"""

i=0
j=0
sum1=0
while i<10 :
    if (i%3==0 or i%5==0):
        sum1 +=i
    i+=1
print("sum :{}".format(sum1))


