'''1.Positional Arguments:-These arguments are those actual arguments,
 which check the formal parameters according to the arrangement 
 of their places during the invocation the function in our program.'''

'''Example'''

# def add(a,b):
#     return a+b

# sum1=add(20,40)
# print(sum1)

# sum2=add(10,30)
# print(sum2)

'''2.Keyword Arguments:-Those actual arguments that check the formal
 parameters with the help of their names, when we call our program,
 no matter at what position they placed. '''

'''Example'''

# def marks(Eng,Maths,Pbi,Hindi):
#     print(Eng)
#     print(Maths)
#     print(Pbi)
#     print(Hindi)
# marks(Maths=80, Hindi=60,Pbi=90,Eng=70)

# def add(a,b,c):
#     return a+b+c
# sum=add(b=10,a=30,c=20)
# print(sum)

'''Default Arguments=In these arguments,it will take default assigned
 value in formal parameters,during the declaraton of the function,if we
   are not giving any value during the invocation of the function,it will
     show the default value as a output.'''

'''Example'''

# def st_detail(sub,name="random"):
#     print(F"subject:{sub}")
#     print(f"student name:{name}")
# st_detail("English")
# st_detail("Maths",name="Jane")
# st_detail(sub="Punjabi",name="honey")

# def st_detail(sub="this",name="random"):
#     print(F"subject:{sub}")
#     print(f"student name:{name}")
# st_detail("English")
# st_detail("Maths",name="Jane")
# st_detail(sub="Punjabi",name="honey")
# st_detail(name="john")

'''Arbitrary argument:-In these arguments we can use *args or **kwargs during
 the declaration of the function which helps in accepting any random argument,
  while the calling of the finction and will show them as a output'''

'''Example:-'''

# def st_detail(**args):
#     for key,value in args.items():
#         print(f"{key}:{value}")
# st_detail(name="Anhad",age=15,cls="tenth")
# st_detail(sub="Maths",marks=90,position="2nd")

# def st_detail(**args):
#     for key,value in args.items():
#         print(f"{value}")
# st_detail(name="Anhad",age=15,cls="tenth")
# st_detail(sub="Maths",marks=90,position="2nd")


