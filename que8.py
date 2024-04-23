#Q WA function to take list of strings as parameter and print all strings which have character 's' 2 times
def display_str(list2):
  for i in list2:
    if i.count("s")==2:
      print(i)

list1=["wiehdss","jdfhinvs","sdhfaiwus","fiussgeurgi"]
display_str(list1)