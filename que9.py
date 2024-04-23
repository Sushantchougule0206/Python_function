#Q WA function to take list of dictionaries. Print all dictionaries which contain key "id".
def display_dict(list2):
  for i in list2:
    for key in i.keys():
      if key=="id":
        print(i["name"])


list1=[{"id":1,"name":"sushant"},{"id":2,"name":"rohan"},{"name":"ashu"}]
display_dict(list1)



def display_dict(list2):
  for i in list2:
    if "id" in i:
        print(i["name"])


list1=[{"id":1,"name":"sushant"},{"id":2,"name":"rohan"},{"name":"ashu"}]
display_dict(list1)
