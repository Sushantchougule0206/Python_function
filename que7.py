#Q WA function to take a dictionary as parameter. Print value of key "name" if key "rollno" is having value 100.
def display_value(dict2):
  if dict2["rollno"]==100:
    print(dict2["Name"])

dict1={"Name":"sushant","rollno":100,"age":22, "city":"kolhapur"}
display_value(dict1)