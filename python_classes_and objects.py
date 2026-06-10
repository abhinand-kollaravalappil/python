# # # # # class car:
# # # # #     def __init__(self,make,model,year):
# # # # #         self.make= make
# # # # #         self.model= model
# # # # #         self.year= year
# # # # #     def display_info(self):
# # # # #         print(f"car:{self.year} {self.model} {self.make}")
# # # # # my_car =car("bmw","m5" ,2021)
# # # # # my_car.display_info()


# # # # # class my_info:
# # # # #     def __init__(self,name,age,place):
# # # # #         self.name=name
# # # # #         self.age=age
# # # # #         self.place=place
# # # # #     def display_info(self):
# # # # #         print(f"my_info: {self.name} {self.age} {self.place}")
# # # # # my_informations= my_info("abhinand",20,"pattambi")
# # # # # my_informations.display_info()


# # # # #acssesing attribute

# # # # # class my_info:
# # # # #     def __init__(self,name,age):
# # # # #         self.name=name
# # # # #         self.age=age
# # # # #     def display_info(self):
# # # # #         print(f"my_info:{self.name}{self.age}")
# # # # # my_informations= my_info("abhinand",20)



# # # # # class bike:
# # # # #     def __init__(self,brand,model,year):
# # # # #         self.brand=brand
# # # # #         self.model=model
# # # # #         self.year=year
# # # # #     def display_info(self):
# # # # #         print(f"bike:{self.brand} {self.model} {self.year}")
# # # # # bike1=bike("yamaha","rx",1993)
# # # # # bike2=bike("honda","cbr",2005)
# # # # # bike3=bike("tvs","max",1999)
# # # # # bike1.display_info()
# # # # # bike2.display_info()
# # # # # bike3.display_info()


# # # # class profil:
# # # #     def __init__(self,name,age,gender):
# # # #         self.name=name
# # # #         self.age=age
# # # #         self.gender=gender
# # # #     def display_info(self):
# # # #         print(f"profil:\t{self.name}\t {self.age}\t {self.gender}\n ")
# # # # profo=profil("anagha",21,"femail")
# # # # profo.display_info()
# # # # #modifing
# # # # profo.name="sivani"
# # # # profo.age=20
# # # # profo.display_info()
# # # # profo.name=("ris")
# # # # profo.age=21
# # # # profo.display_info()

# # # class car:
# # #     def __init__ (self,brand,name,price):
# # #         self.brand=brand
# # #         self.name=name
# # #         self.price=price
# # #     def display_info(self):
# # #         print(f"car: {self.brand} {self.name} {self.price}")
# # # car1=car("bmw","m4",3000000)
# # # car1.display_info()
# # # print(car1.brand)
# # # car1.brand="honda"
# # # car1.display_info()
# # # print(car1.brand)


# # class Car:
# #     def __init__ (self,brand,name,price):
# #         self.brand=brand
# #         self.name=name
# #         self.price=price
# #     def __str__(self):
# #         return f"car: {self.brand} {self.name} {self.price}"
# # car1=Car("bmw","m4",40000)
# # print(car1)

# #instance varible

# # class Employe:
# #     company="softronics"
# #     def __init__(self,name,position):
# #         self.name=name
# #         self.position=position
# # emp1=Employe("jhon","manger")
# # emp2=Employe("alice","developer")
# # print(emp1.company)
# # print(emp2.company)

# # print(emp1.name)
# # print(emp2.name)

# #decrators
# #1class method


# class Company:
#     Company_name="tech inoverters"

#     @classmethod
#     def change_Company_name(cls,new_name):
#         cls.Company_name=new_name
# Company.change_Company_name("futer solutions")
# print(Company.Company_name)


#STATIC METHOD

# class Mathoparation:
#     @staticmethod
#     def add (a,b):
#         return a+b
# print(Mathoparation.add(10,30))