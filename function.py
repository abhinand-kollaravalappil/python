#def  greet (name,age,place):
   #print(f" my name {name},age{age},fromm{place}")

#greet ("alice",21,"new york")

#def greet (name,age,place):
   #print(f"my name is{name},my age is{age},im from {place}")
#greet("jhon",22,"kochi")



#def add (a,b):
    #"""this function adds two numbers"""
    #return a+b
#print(add.__doc__)


#def cheak_number(num):
 # if num>0:
  #    print("positive")
  #elif num<0:
   #   print("negative")
#cheak_number(10)
#cheak_number(-5)

#def cheak_even_odd(num):
   #if num %2==0:
    #  print("even number")
   #elif num %2!=0:
    #  print("odd number")

#cheak_even_odd(5)
#cheak_even_odd(12)


# def add():
#    print(10+20)
# add()

#add=lambda a,b:a+b
#print(add(10,20))

#lamba with_reduce()
#numbers=[1,2,3,4]
#sum_reduce=(lambda x,y:+y,numbers)
#print(sum_reduce)

#using filter()
#numbers=[1,2,3,4,5,6]
#even_numbers=filter(lambda x:x%2==0,numbers)
#print(list(even_numbers))

#higher_order_function
#def calulate(a,b,oprater):
   #return oprater(a,b)

#add=lambda x,y:x+y
#sub=lambda x,y:x-y
#multi=lambda x,y:x*y
#devide=lambda x,y:x/y

#print(calulate(10,20,add))
#print(calulate(10,20,sub))
#print(calulate(10,20,multi))
#print(calulate(10,20,devide))

#def multiply (a,b):
   
 #  result=multiply(4,5)
#print(result)


#x=10
#def_outer_function():

#x=5  #enclosing_scop
#def_inner_function():
#   x=2
#   print
#outer_function
#print(x)

#def greet():   #local_scop
#   name="abhi"
#   print(name)
#greet()

#global_scop
#name="abhi"
#def greet():
#   print(name)
#greet()
#print(name)

#arbitary arguments

#def numbers(*num):
#   print(num)
#   numbers(10,20,30)

#def add(*numbers):
#   print(sum(numbers))
#add(1,2,3)
#add(10,20,30,40)

#keyword arguments

#def detiils(**data):
#   print(data)
#detiils(nmae="abu",age=40)

#def sum_numbers(*arg):
#   total=0
#   for numbers in arg:
#      total+=numbers
#   return total
#result=sum_numbers(1,2,3,4,5)
#print(result)

#def print_detiles(**kwargs):
#   for key,value in kwargs.items():
#      print(f"{key}:{value}")
#print_detiles(name="alice",age=30,city="newyork")


#using *arg and **kwargs together
#def display_info(*arg,**kwarg):
#   print("positional argument:",arg)
#   print("keyword argument:",kwarg)
#display_info(1,2,3,name="alice",age=25)



