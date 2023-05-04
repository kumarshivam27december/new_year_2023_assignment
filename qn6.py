# s=str(input())
# for i in range(1,len(s)+1):
#     if i==len(s):
#         print(s[i-1]*i,end="\n")
#     else:
#         print(s[i-1]*i,end="")
    

# def getsum(n):
#     for digit in str(n):
#         sum += int(digit)
#     return sum
# n=1234
# print(getsum(n))
            
# def  sumDigits(no):
#     return 0 if no==0 else int(no%10) + sumDigits(int(no/10))
    
# n=int(input())
# print(sumDigits(n))
    
# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         b=sum(i)
#         print(b)
       
       
       
def factor (num):
    factor=[1]
    for i in range (2,num+1):
        if num%i==0:
            factor.append(i)
    return sum(factor)       
n=int(input())
print(factor(n))   
