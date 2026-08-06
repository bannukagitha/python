word="Python Programming"
part="Computer"
print(word)
print(word[0])#first character of the string
print(word[-1])#last character of the string
print(word[2])#third character of the string
print(word[-2])#second last character of the string
name="kagitha bhanu durga prasad"
print("all characters of the string are:")
print(name[0],name[1],name[2],name[3],name[4],name[5],name[6],name[7],name[8],name[9],name[10],name[11],name[12],name[13],name[14],name[15],name[16],name[17],name[18],name[19],name[20],sep="\n")
print(name[0],name[-len(name)])#first and first character of the string using positive and negative indexing
print(name[len(name)-1],name[-1])#last and last character of the string using positive and negative indexing
print(word[len(word)//2])#middle character of the string
#print(part[9])#give indexerror because the index is out of range
print(part[-1])#correct output because the index is in range
Word = "Programming"

print(Word[:4])#returns the first four characters of the string
print(Word[4:])#returns the characters from index 4 to the end of the string
print(Word[2:6])#returns the characters from index 2 to index 5 of the string
print(Word[3:3])#returns an empty string because the start and end index are same
print(Word[10:50])#returns the characters from index 10 to the end of the string because the end index is out of range gives the empty string
text = "Engineering"
print(text[0:5])#returns the first five characters of the string
print(text[3:])#returns the characters from index 3  of the string
print(text[7:])#returns the characters from index 7  of the string
print(text[:])#returns all characters of the string
print(text[4:4])#returns an empty string because the start and end index are same
print(text[20:30])#returns an empty string because the start and end index are out of range
print(text[:100])#returns all characters of the string because the end index is out of range
a="Python"
b="Python"
print(a==b)#returns True because both strings are equal
print(a is b)#returns True because both strings are same object in memory
print(id(a),id(b))#returns the memory address of both strings
x="bhanu"
y=x
print(id(x),id(y))#returns the same memory address of both strings because both strings are same object in memory
y="java"
print(id(x),id(y))#now the memory address of y is different because it is assigned a new string value
n=input("Enter a number: ")
m="dragon"
print(n==m)#returns True if the input number is equal to the string "dragon" otherwise returns False
print(n is m)#returns True if the input number is the same object in memory as the string "dragon" otherwise returns False
print("Equality operator (==) is used to compare the values of two strings and returns True or False.")
print("Identity operator (is) is used to compare the memory address of two strings and returns True or False.")
print("STRING METHODS")
name = "bhanu"
college = "SRKR Engineering College"
text = "PyThOn Is AwEsOmE"
print(name.upper())#returns the string in uppercase
print(name.lower())#returns the string in lowercase
print(name.split())#returns a list of words in the string
print(name.replace("b","B"))#returns the string with the specified character replaced
print(name.strip())#returns the string with leading and trailing whitespace removed
print(college.upper())#returns the string in uppercase
print(college.lower())#returns the string in lowercase
print(college.split())#returns a list of words in the string
print(college.replace("SRKR","srkr"))#returns the string with the specified character replaced
print(college.strip())#returns the string with leading and trailing whitespace removed
print(text.upper())#returns the string in uppercase
print(text.lower())#returns the string in lowercase
print(text.split())#returns a list of words in the string
print(text.replace("PyThOn","python"))#returns the string with the specified character replaced
print(text.strip())#returns the string with leading and trailing whitespace removed
k=input("Enter a string: ")
if k.lower() == "yes":
    print("You entered yes")
else:
    print("You did not enter yes")
print("upppercase() method is used to convert the string to uppercase.")
