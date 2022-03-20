name = input("what is your name? :")
age = input("what is your age?: ")
city = input("which city do you live in? :")
fun = input ("what do you enjoy? :")
print(name)
print(age)
print(city)
print(fun)

string = "name {},age {},city {},fun {}"
output= string.format(name,age,city,fun)
print(output)
