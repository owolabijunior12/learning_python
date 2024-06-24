from enum import Enum
from datetime import date
from smtplib import SMTP
from lib.text import demoUserData
from sys import argv

print(argv)
# server =SMTP("localhost:8080")
# server.sendmail(
#     from_addr="owolabijunior12@gmail.com",
#     to_addrs="iboytech.info@gmail.com",
#     msg="hello am here"
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
_newList =["iboytech",21,True,"hello"]
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