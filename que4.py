#Q WA function to check if number is prime or not. Return True if number is prime and false if number not prime.
def prime(num):
  if num<2:
    return False
  
  for i in range(2,int(num**0.5)+1):
    if num%i==0:
      return False
  
  return True

number=int(input("Enter the number:"))
print(prime(number))