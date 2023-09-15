#calculate the factorial number of a given number 
def factorial_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial_rec(n-1)
number=int(input("enter a value:"))
res=factorial_rec(number)
print("the factorial of {} is {}".format(number,res))