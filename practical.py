#def greet(name):
#    return f"hello,{name}"


#def info(name):
#    return f"iam",  {name}


# 1 mathamatical functions (math)
#import math
#print(math.sqrt(22))


#2
#date and time functions(datetime):
#from datetime import datetime
#now=datetime.now()
#print(now)



#intercasting with the oprating system(os):
#import os
#current_dir= os.getcwd()
#print(current_dir)

#4
#working with json data(e.json:)
#import json
#data={"name":"jhon","age":30}
#parsed_data=json.loads(data)
#print(parsed_data)

#from datetime import datetime
#now =datetime.now()
#print(now)
try:
    my_dict={
        "name":"abhi",
        "age":32,
        "city":"pattambi"}
    

except Exception:
    print("dork", )

# class profil:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def display_info(self):
#         print(f"profil:\t{self.name}\t {self.age}\t {self.gender}\n ")
# profo=profil("anagha",21,"femail")
# profo.display_info()
# #modifing
# profo.name="sivani"
# profo.age=20
# profo.display_info()
# profo.name=("ris")
# profo.age=21
# profo.display_info()

# class MYERROR (Exception):
#     pass
# age=16
# try:
#     if age <18:
#         raise MYERROR("not allowed")
#     print("redy to vote")
# except MYERROR as e:
#     print(e)