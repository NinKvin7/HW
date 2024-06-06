#print("hello world")

#print('hello world')

#print(type('a'))

# a = 1
# b = "m"
# print(a, b, "9", sep="---", end="\n")
# print(a, b, id(b), sep="---", end="t1")

# print(len(" 22n"))

# k = "nino"
# text = f""" Happy
# bday {k} """
# print(text)

# t = str(3)
# print(type(t))


# word = input("dawere rame ")
# print("hello", word)

 # ------------------------------------------homework

#დაწერე პროგრამა, რომელიც გეკითხება სახელს, გვარს და ბეჭდავს ინფორმაციას
#1
# name = input("write your name: ")
# surname = input("write your surname: ")
# print(name, surname)

#2
# a = float(input("write first number: "))
# b = float(input("write second number: "))
# print(a ** b)

#3
# დაწერე პროგრამა რომელიც გეკითხება სახელს, გვარს, ასაკს და ქალაქს და ბეჭდავს ინფორმაციას
# name = input("write your name: ")
# surname = input("write your surname: ")
# age = input("write your age: ")
# city = input("write the city where you live: ")
# text = f""" Name: {name}
# Surname: {surname}
# Age: {age}
# City: {city}"""
# print(text)

#4
# დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ნებისმიერი სამი სხვადასხვა ხილის
# დასახელება ცალცალკე. რეზულტატი კი იბეჭდება შემდეგი სახით:
# Apple//Peach%%Orange
#
# a = input("Name the fruit: ")
# b = input("Another fruit: ")
# c = input("One more please: ")
# text = f"""{a}//{b}%%{c}"""
# print(text)

#5
# დაწერე პროგრამა,რომელიც გთხოვს, შეიყვანო ტექსტი, დათვლის მასში არსებული
# სიმბოლოების რაოდენობას და გამოიტანს შედეგს შემდეგნაირად: Number of symbols: 50
#
# a = input("Write the text, please: ")
# length = len(a)
# text = f"""Number of symbols: {length}"""
# print(text)

###########################

# name = input("write your name: ").lower
# if name == "bond":
#     print("wellcome on board 007")
# else:
#     print(f"Good morning {name}")




grade = int(input("shemoiyvanet qula: "))
if grade <60 :
    print ("grade: D")
elif grade <80 :
    print ("grade: C")
elif grade <90 :
    print ("grade: B")
else:
    print("grade: A")