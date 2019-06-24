print("Akshay")
#a = input("Enter your name here ")
#print(a)

#age = input("Enter your Age ")
age = 15
age = int(age) + 5
print(age)
print("Akshay bengani age is ",age)

if(age==15):
    print("true")
elif(age==20):
    print("true")
else:
    print("false")

big = max("HelloWorld")
small = min("HelloWorld")
print(big)
print(small)

def greet(lang):
    if lang == "en":
        return "Hello"
    elif lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hi"

print(greet("en"),'there')
print(greet("es"),"toiuj")
print(greet("fr"),"kvdf")
print(greet("sv"),"ufvhksv")

for i in [5,4,3,2,1]:
    print(i)

fruit = "banana"
letter = fruit[1]
print("Banana Letter at 2nd Position ",letter)
print("Banana length is ",len(fruit))
name = "AKshay Bengani"
nameInSmall = name.lower()
print(nameInSmall)
nameInCapital = name.upper()
print(nameInCapital)

s = "Monty Python"
print(s[0:4])
print(s[:5])
print(s[6:])
print(s[:])

data = "From akshay.16BCAN018@jecrcu.edu.in Wed Jan 23 06:11:16 2019"
startpos = data.find("@")
endpos = data.find(" ",startpos)
host = data[startpos + 1 : endpos]
print(host)

print("n" in fruit)
print("m" in fruit)

if "a" in fruit:
    print("Found it")

count = 0
fhand = open('tut1.py','r')
for lines in fhand:
    print(lines)
    count = count + 1
print("Total number of lines are ",count)






