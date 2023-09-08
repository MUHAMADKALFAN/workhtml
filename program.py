#  if(5>2):
#      print("8")
#  else:
#     print("41")
# if(5<2):
#     print("8")
# elif(5>2):
#     print("41")
    
a=int(input("enter number of a="))
b=int(input("enter number of b="))
c=int(input("enter number of c="))
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
elif(b>a):
        if(b>c):
            print(b)
        else:
            print(c)
elif(c>a):
        if(c>b):
            print(a)
        else:
            print(c)
else:
     print(b)