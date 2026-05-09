# creating a dictionarie
#my_dict={
    # "name":"abhi",
    # "age":20,
    # "mark":90
#}
#print(my_dict)

#using the dict()

#another_dict=dict(name="abhi",age=20,city="los angles")
#print(another_dict)

#empty dict

#empty_dict={}
#print(empty_dict)

#accesing with brackets
#my_dict={"name":"jhon","age":20,"city":"los angles"}

#print(my_dict)

#chainging dictionary items
#my_dict={"name":"jhon","age":30}
#my_dict["age"]=31
#print(my_dict)

#addings iteams to a dictionary
#my_dict={"name":"jhon","age":30}
#my_dict["city"]="newyork"
#print(my_dict)

#removing iteams to a dictionary
#my_dict={"name":"jhon","age":30,"city":"newyork"}
#age=my_dict.pop("age")
#print(age)

#pop iteam
#my_dict={"name":"jhonn","age":30}
#result=my_dict.popitem("age")
#print(result)

#del statment
#my_dict={"name":"jhon","age":30}
#del my_dict["age"]
#print(my_dict)

#copying a dictionary
#using copy()
#orginal={"name":"jhon","age":30}
#copy_dict=orginal.copy()
#print(copy_dict)

#using dict ()constructer
#orginal={"name":"jhon","age":30}
#copy_dict=dict(orginal)
#print(copy_dict)

#nested dictionaries
#nested_dict={
    #"person1":{"name":"jhon","age":30},
   # "person2":{"name":"alice","age":25}
    
#}
#print(nested_dict["person1"]["name"])

#dictionary mwthod
#key()
#my_dict={"name":"jhon","age":30}
#print(my_dict.keys())

#values
#print(my_dict.values())
#items
#print(my_dict.items())

#update
#my_dict={"name":"jhon","age":30}
#my_dict.update({"city":"newyork","age":31})
#print(my_dict)

#from keys
#keys=["name","age","city"]
#new_dict=dict.fromkeys(keys,"uknown")
#print(new_dict)

#set default
#my_dict={"name":"jhon","age":40}
#city=my_dict.setdefault("city","newyork")
#print(city)

