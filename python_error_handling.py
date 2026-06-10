#error handling in python

#syntax error
#print("hello"

#zero division error
#a=4
#b=0
#result=(a/b)
#print(result)

#type error
#x="10"
#y=3
#print(x+y)

#value error
#x=int("hello")
#print(x)

#index error
#my_list=[1,2,3,4,5,]
#print(my_list[5])

#key error
#my_dict={
#    "name":"abhi",
#    "age":21
#}
#print(my_dict["marks"])

#file found error
#abc=open("sdh.txt""r")
#abc.close

#expection handling with try_expet
#try:
#    x=10/0
#except ZeroDivisionError:
#    print("u cant divide by zero")

#using else and finaly in excepion handling

#try:
#    num=int(input("enter a number :"))
#    result=10/num
#except ZeroDivisionError:
#    print("division by zero not allowed")
#else:
#    print(f"the result is{result}")
#finally:
#    print("this will allways be printed")

#raising expection

#x=-5
#if x<0:
#    raise ValueError("negative number  are not allowed")

#CUSTOM ERROR
#class NegativeNumberError(Exception):
#       pass
#def cheak_number(num):
#    if num<0:
#       raise NegativeNumberError("who are you")
#try:
#       cheak_number(-10)
#except NegativeNumberError as e:
#        print(e)