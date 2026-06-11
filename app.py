# from flask import Flask
# app= Flask(__name__)

# @app.route('/')
# def home():
#     return "hello buddy how are you"
# if __name__=="__main__":
#      app.run(debug=True)

#encapsulations

# class  Employe:

#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#     def display_employe (self):
#         print(f"name:{self.name},salary:{self.__salary}")
#     def update_salary(self,new_salary):
#         self.__salary=new_salary
# emp=Employe("jhon",50000)
# emp.display_employe()

# class Employe:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display__info(self):
#         print(f"Employe:{self.name} {self.salary}")
# emp=Employe("jhon",23000)
# emp.display__info()

class Employe:
    def __init__(self,name,salary):
        self.name=name  #public attribute

        self.__salary=salary  #private attribute
    def display__info(self):
        print(f"Employe:{self.name} {self.__salary}")
    def update_salary(self,new_salary):
        self.__salary=new_salary
emp=Employe("jhon",50000)
emp.display__info()