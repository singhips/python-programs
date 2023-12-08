def add():
    print(a+b)
def sub():
    print(a-b)
def divid():
    print(a/b)
def multi():
    print(a*b)
number=int(input("Enter 1 For Addition \nEnter 2 For Subtrution\nEnter 3 For Divition\nEnter 4 Multiply\nEnter Your Choice:- "))
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
if number==1:
    print(add())
elif number==2:
    print(sub())
elif number==3:
    print(divid())
elif number==4:
    print(multi())
else:
    print("Enter Only 1-4 Only")