import math
def perfectNumber(num):
    n = math.ceil(pow(num,0.5))
    sum=1
    for i in range(2,(n+1)):
        if num%i==0:
            sum+=i
            if num % (num // i)==0 and (num//i) !=i:
                sum+= num//i
    if sum == num:
        return True
    else:
        return False
print(perfectNumber(28))