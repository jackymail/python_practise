import re

allApes = re.findall('ape.', "the ape was at the apex")

for i in allApes:
    print (i)


theStr = "The ape was at the apex"

for i in re.finditer("ape.",theStr):
    locTuple = i.span()
    print (locTuple)
#(19, 23)
    print(theStr[locTuple[0]:locTuple[1]])

animalStr = "Cat rat mat pat"

allAnimals = re.findall("[Crmfp]at",animalStr)

for i in allAnimals:
    print(i)

#someAnimals = re.findall("[c-mC-M]]",animalStr)
someAnimals = re.findall("[^Cr]]",animalStr)  #string with C and r

for i in someAnimals:
    print(i)

# replace letters
owlFood = "rat cat mat pat"

regex = re.compile("[cr]at]")

owlFood = regex.sub("owl",owlFood)

print(owlFood)

randStr = "Here is  \\stuff"

#print("find \\stuff :",re.search("\\\\stuff",randStr))
print("find \\stuff :",re.search(r"\\stuff",randStr))



randStr1 = "F.B.I. I.R.S. CIA"
print("Matched :",len(re.findall(".\..\.. \.",randStr1)))


randStr3 = '''This is a long
string that goes
on for many lines
'''
print (randStr3)
regex = re.compile("\n")
randStr3 = regex.sub(" ",randStr3)
print(randStr3)

#\d : [0~9]
#\D : [^0~9]
#
randStr4 = "12345"
print("Matches numbers :",len(re.findall("\d",randStr4)))
print("Matches number 5:",len(re.findall("\d{5}",randStr4)))

numStr = "123 12345 123456 1234567"

print("Matches :",len(re.findall("\d{5,7}",numStr)))

phNum = "412-555-1212"
if re.search("\w{3}-\w{3}-\w{4}",phNum):
    print("It is a phone number");

if re.search("\w{2,20}","Ultraman"):
    print("It is a valid one")

if re.search("\w{2,20}\s\w{2,20}","Toshio Muramachu"):
    print("It is valid");

print("Matches :",len(re.findall("a+","a as ape bug")))


















