from enum import Enum
  
class iboytech(Enum):
    INACTIVE = 0  
    ACTIVE =1

print(list(iboytech))
# age = input("What is your Age?  ")
# print(f'Am {age}  years  of age')

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
myList[1]["name"] = "iboytech"
print(myList)

_newList =["iboytech",21,True,"hello"]
_newList.sort(key=bool)
print(_newList)