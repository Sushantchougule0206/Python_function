#Q WA function to take list as parameter and print all numbers of given list which are divisible by 11
def divisible_11(num_list):
  for i in num_list:
    if i%11==0:
      print(i)
      
numbers=[11,44,35,77,56,33]
divisible_11(numbers)