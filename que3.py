#Q WA function to take string as parameter
#Check if string is palindrome or not
#If palindrome return 1
#if not palindrome return 0

def palindrome(string):
  if string[::-1]==string:
    return 1
  else:
    return 0

demo_str=input("Enter the string:")
demo_str=demo_str.lower()
print(palindrome(demo_str))