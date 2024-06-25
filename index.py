from enum import Enum
from datetime import date
from smtplib import SMTP
from lib.text import demoUserData
from sys import argv
from argparse  import ArgumentParser
from functools import reduce
print(argv)
# server =SMTP("localhost:8080")
# server.sendmail(
#     from_addr="owolabijunior12@gmail.com",
#     to_addrs="iboytech.info@gmail.com",
#     msg="hello am here",
# )



print(demoUserData)
class iboytech(Enum):
    INACTIVE = 0   
    ACTIVE =1

print(list(iboytech))
age = input("What is your Age?  ")
print(f'Am {age}   years  of age')

# lists
myList =[
    {
        "name":"Owolabi Destiny",
        "dept": "software Engineerimg",
        "stack":["javascript","python","c++","tailwindcss","redux","css","material UI"],
        "education":"Bs.c,OND"
    },
    {
        "name":"osho samuel",
        "dept": "software Engineerimg",
        "stack":["javascript","python","tailwindcss","redux","css"],
        "education":"Bs.c,OND"
    }
]
print(f"iboytech is here learning python on the {date.today()}")  # type: ignore

del myList[0]
print(myList)
_newList =["iboytech",21,True,"hello",]
_newList.pop()
print(_newList)
#  set
my_list = {"hello", "me", 3 ,4} 
_my_list = {"hello","3",3}
p = my_list > _my_list
print(p)

def counter():
    count = 0
    def increasement():
        nonlocal count
        count+=1
        return count
    return increasement 
  
checker = counter()
print(checker())
print(checker())
print(checker())
print(checker())
print(checker())



# loop
# while loop
condition =0 
while condition < 12:
    print("condition is true")
    condition +=1
print("after loop")  
# for loop
iteems =[1,2,3,4,5,6]
for e,f in enumerate(iteems):
    print(e,f)

# for i in range(0,13,3):
#     print(i)
class Animal:
    def walk(self) -> None:
         return "hello...................."
        
class dog(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age =age
        pass
    def bark(self):
        print("woof!")
  
print(dog("iboytech",24).name)
print(dog("iboytech",24).age)
dog("iboytech",24).bark()
print(dog("iboytech",24).walk())

s= "hello, I'm {} a software engineer from yabatech"
print(s.format(iboytech))
parser = ArgumentParser(
    description="This is to tell iboytech to the world! inshallah📿"
)

parser.add_argument("-c", "--color", metavar="color", required=True,choices={"red","blue","yellow"}, help="the help color to search for")
args= parser.parse_args()
print(args.color)


# map()
number =[1,2,3,4,5,6,7,8,9]

def double(a):
    return a

hell = lambda b : b * 2

result = map( hell, number)
print(list(result))
print(list(number))
# filter
def isEven(n):
    return n % 2 == 0

isEven2 = lambda n : n % 2 == 0 

result2 = filter(isEven, number)
result3 = filter(isEven2, number)
print(list(result2))
print(list(result3))


expenses = [
    ("dinner",80),
    ("dinner",80),
    ("car_repair",2)
]

sum = 0
for exp in expenses:
    sum += exp[1]
 
exp2 = lambda a, b: a[1] + b[1] 
sum2 = reduce(exp2,expenses)   
print(sum)    
print(sum2)    
  
