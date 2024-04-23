#Q WA function to take a string as parameter. Print its alternate characters starting from 2nd character
def alternate_string(str1):
  for i in range(1,len(str1),2):
      print(str1[i])
    
string="Sushant"
alternate_string(string)