#Q. WA function to take a number as parameter and  print True if given number is even else print False

def even_odd(num):
    if num%2==0:
        return True
    else:
        return False
    
number=int(input("Enter the number:"))
print(even_odd(number))