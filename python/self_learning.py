thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2000
}

print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2000}
print(len(thisdict)) # 3

typedict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(typedict) # {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}
print(type(typedict)) # <class 'dict'>

adict = dict(name = "John", age = 36, country = "Norway")
print(adict) # {'name': 'John', 'age': 36, 'country': 'Norway'}
print(adict.get("name")) #John
print(adict.keys()) #dict_keys(['name', 'age', 'country'])
print(adict.values()) #dict_values(['John', 36, 'Norway'])

del adict["country"]
print(adict) #{'name': 'John', 'age': 36}

for char in adict:
    print(char) #name age
    print(adict[char])
    print(adict.values())

i=0
while i<6:
    i=i+1
    if i == 3:
        continue
    print(i)

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
finally:
   print("is finishied")

try:
  print(x)
except:
  print("Variable x is not defined")
else:
  print("Something else went wrong")
finally:
   print("is finishied")
