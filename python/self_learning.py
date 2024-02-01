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


def test(string, str):
    last_position = -1
    while True:
        position = string.find(str, last_position+1)
        if position == -1:
            return last_position
        last_position = position


print(test('hi how are you hello world, hello yoyo!', 'hello'))


while True:
    try:
        num = int(input('Input：'))
    except ValueError: 
        print("Invaild！")
        continue
    if num % 2 == 0:
        print('Even number')
    else:
        print('Odd number')
    break

def trim(s):
    flag = 0
    if s[:1]==' ':
        s = s[1:]
        flag = 1
    if s[-1:] == ' ':
        s = s[:-1]
        flag = 1
    if flag==1:
        return    trim(s)
    else:
        return s
print(trim('  Hello world!  '))

def trim(s):
    while(True):
        flag = 0
        if s[:1]==' ':
            s = s[1:]
            flag = 1
        if s[-1:] == ' ':
            s = s[:-1]
            flag = 1
        if flag==0:
            break
    return s
print(trim('  Hello world!  '))

def test():
    n = 8
    for i in range(-int(n/2), int(n/2) + 1):
        print(" "*abs(i), "*"*abs(n-abs(i)*2))


print(test())


def test(sum_to):
    
    sum_all = 0
    for i in range(1, sum_to + 1):
        sum_all += i * (-1) ** (1 + i)
    return sum_all


if __name__ == '__main__':
    result = test(sum_to=100)
    print(result)
