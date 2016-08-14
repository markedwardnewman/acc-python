import Proj06Runner

str = 'The lazy brown fox jumped over the fence.'
sep = ' ' #a space character

result = Proj06Runner.run(str,sep)
for word in result:
    print(word)

print()
str = 'The lazy brown fox jumped over the fence.'
sep = 'o' #This is a lower-case O character

result = Proj06Runner.run(str,sep)
for word in result:
    print(word)