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
m = "banana"

print(m.find("a"))#returns the index of the first occurrence of the specified character in the string   
print(m.rfind("a"))#returns the index of the last occurrence of the specified character in the string
print(m.count("a"))#returns the number of occurrences of the specified character in the string
print(m.startswith("ba"))#returns True if the string starts with the specified character otherwise returns False
print(m.endswith("na"))#returns True if the string ends with the specified character otherwise returns False
print(m.find("x"))#returns -1 because the specified character is not found in the string
print("find() method is used to find the index of the first occurrence of the specified character in the string if not in sting  returns -1.")
print("index() method is used to find the index of the first occurrence of the specified character in the string and raises a ValueError if the character is not found.")
print("rfind() method is used to find the index of the last occurrence of the specified character in the string if not in sting  returns -1.")
print("count() method is used to count the number of occurrences of the specified character in the string.")
print("startswith() method is used to check if the string starts with the specified character and returns True or False.")
print("endswith() method is used to check if the string ends with the specified character and returns True or False.")
k="Python Programming Language"
print(k.find("Programming"))#returns the index of the first occurrence of the specified substring in the string
print(k.find("Language"))#returns the index of the first occurrence of the specified substring in the string
print(k.count("a"))#returns the number of occurrences of the specified substring in the string
print(k.count("m"))#returns the number of occurrences of the specified substring in the string
print(k.startswith("Python"))#returns True if the string starts with the specified substring otherwise returns False
print(k.endswith("Language"))#returns True if the string ends with the specified substring otherwise returns False
print(k.find("Java"))#returns -1 because the specified substring is not found in the string
#print(k.index("Java"))#raises a ValueError because the specified substring is not found in the string
print(k.count("z"))#returns 0 because the specified substring is not found in the string

text1 = "   Python   "

print(text1.strip())#returns the string with leading and trailing whitespace removed
print(text1.lstrip())#returns the string with leading whitespace removed
print(text1.rstrip())#returns the string with trailing whitespace removed
text2= "cat cat cat"

print(text2.replace("cat", "dog", 2))#returns the string with the first two occurrences of the specified substring replaced
print("45".zfill(5))#returns the string with leading zeros added to make the string length equal to the specified width
print("Python".center(12, "-"))#returns the string centered in a string of the specified width with the specified fill character
print("difference between strip(),replace(),is used to remove leading and trailing whitespace from the string,replace() is used to replace a specified substring with another substring in the string.")
print("Can replace() replace only one occurrence?:YES")
print("Which method removes tabs?:strip()")
print("Do these methods modify the original string?:NO,they return a new string with the modifications applied.")
username = input("Enter username: ")

username = username.strip().lower()

if username == "bhanu":#checks if the username is equal to "bhanu" after removing leading and trailing whitespace and converting to lowercase
    print("Welcome!")

sentence = "I love Python programming"
print(sentence.split())#returns a list of words in the string
words = ["I", "love", "Python"]
print(" ".join(words))#returns a string by joining the list of words with a space as the separator
data = "Bhanu,20,CSIT,SRKR"
print(data.split(","))#returns a list of values in the string by splitting the string at each comma
date = "08-08-2026"
print(date.split("-"))#returns a list of values in the string by splitting the string at each hyphen
path = "C:/Users/Bhanu/Desktop/python/file.py"
print(path.rsplit("/", 1))#returns a list of values in the string by splitting the string at the last occurrence of the specified separator
letters = ["P", "y", "t", "h", "o", "n"]
print("".join(letters))#returns a string by joining the list of letters with an empty string as the separator
text4 = "Python is powerful"
dummy = text4.split()
print("-".join(dummy))#returns a string by joining the list of words with a hyphen as the separator
email = "bhanu@gmail.com"
print(email.partition("@"))#returns a tuple containing the part before the separator, the separator itself, and the part after the separator
given_string = "Python    is     very    powerful"
dummy1 = given_string.split()
print("-".join(dummy1))#returns a string by joining the list of words with a hyphen as the separator

text = "  Python Programming  "

print(text.strip())#returns the string with leading and trailing whitespace removed
print(text.upper())#returns the string in uppercase
print(text.lower())#returns the string in lowercase
print(text.find("Programming"))#returns the index of the first occurrence of the specified substring in the string
print(text.count("m"))#returns the number of occurrences of the specified character in the string
print("Python" in text)#returns True if the specified substring is found in the string otherwise returns False
print(text.startswith("Python"))#returns True if the string starts with the specified substring otherwise returns False
print(text.strip().startswith("Python"))#returns True if the string starts with the specified substring after removing leading and trailing whitespace otherwise returns False
print(text.split())#returns a list of words in the string
print("-".join(text.split()))#returns a string by joining the list of words with a hyphen as the separator
print("NOTE: The methods used in this code do not modify the original string, they return a new string with the modifications applied.")

final = "  Python   is   powerful  "

a = final.strip()#returns the string with leading and trailing whitespace removed
b = final.split()#returns a list of words in the string
c = "-".join(b)#returns a string by joining the list of words with a hyphen as the separator

print(final)#returns the original string with leading and trailing whitespace
print(a)#returns the string with leading and trailing whitespace removed
print(b)#returns a list of words in the string
print(c)#returns a string by joining the list of words with a hyphen as the separator