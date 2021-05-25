print('Hello ' + 'Welcome to pyhton class')#joining of two strings together
print('Hello' + ' ' + 'World') #with empty 

#joining of variable and string with + and ,
Firstword = 'Simeon'
print('Welcome to python class ' + Firstword)
print('Welcome to python class', Firstword)

#joining of two variables with + and ,
Firstname = 'Noel'
Secondname = 'Kamson'
print(Firstname, Secondname)
print(Firstname + ' ' + Secondname )

#Datatype conversion
num3 = '5'
print(float(num3))
num = 5
num2 = 2.5
word = 'Tope'
print(int(num2)) #converting float to integer

#convert the following
x = 58 #convert to float
y = 100.56 #convert to str
z = 105.5 #convert to int
a = '8' #convert to int and float

print(float(x)) 
print(str(y))
print(int(z))
print(int(a))
print(float(a))

#string slicing using square bracket
name = 'Chris'
print(name[0:3])

#string formating #curly bracket is what holds our value
num = 5
num2 = 10
num3 = 15
statement = 'i have {} pairs of shoes, {} suits and {} jackets'
print(statement.format(num2,num,num3))

#another way to format variables into statement
firstname = 'Bright'
secondname = 'Chuks'
course = 'Python'
print(f"Welocme {firstname} {secondname} to {course} class")

#Upper function in string method
fullname = 'oyategbe-bose christianah adeoti'
print(fullname.upper())
fullname = 'oyategbe-bose christianah adeoti'
print(fullname.lower())
fullname = 'oyategbe-bose christianah adeoti'
print(fullname.capitalize())
fullname = 'oyategbe-bose christianah adeoti'
print(fullname.split())
word = 'info@earlycode.com'
print(word.strip())

















