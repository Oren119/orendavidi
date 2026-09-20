# File: homework1.py
#                      --- Variables and Data Types ---
#V1 - Integer
a = 10
print(a) 
print(type(a))

#V2 - Float
b=1.5
print(b)
print(type(b))

#V3 - String
c = "3j"
print(c)
print(type(c))

#V4 - String
d = "hello"
print(d)
print(type(d))

#V5 - List
e = [1, 2, 3]
print(e)
print(type(e))

#V6 - Dictionary
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))

#V7 - Tuple
g=(1,2)
print(g)
print(type(g))

#V8 - List
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))

#V9 - Boolean
i = True
print(i)
print(type(i))

#V10 - None
j = None
print(j)
print(type(j))

#V11 - List
k = [True, "blue", 12]
print(k)
print(type(k))

#V12 - String
l = str(14)
print(l)
print(type(l))

#V13 - Float
m= 1e4
print(m)
print(type(m))

'''
1. Eight different data types 
2. - Integer, Float, String List, Dictionary, Tuple, Boolean, None
3. c, d, and l are strings. b and m are floats. e, h, and k are lists
4. l is a string. str stands for string and creates anything declared into a string
5. Another datatype would be binary (bytes):
'''
n = b"Hello World"
print(n)
print(type(n))

#                    --- Booleans ---
print(10>9) #True, 10 is greater than 9
print(10==9) #False, 10 is not equal to 9
print(10<=9) #False, 10 is not less than or equal to 9
print(bool("abc")) #True, non-empty string is True
print(bool(["apple", "cherry", "bannana"])) #True, non-empty list is True
print(bool(True)) #True, True is True
print(bool(False)) #False, False is False
print(bool(0)) #False, 0 is False
print(bool("")) #False, empty string is False
print(bool(" ")) #True, non-empty string is True
print(bool(())) #False, empty tuple is False
print(bool([])) #False, empty list is False
print(bool({})) #False, empty dictionary is False
print(bool(True and False)) #False, True and False is False
print(bool(True and True)) #True, True and True is True
print(bool(False and False)) #False, False and False is False
print(bool(True or False)) #True, True or False is True
print(bool(True or True)) #True, True or True is True
print(bool(False or False)) #False, False or False is False
print(bool(not(False))) #True, not False is True
print(bool(not(True))) #False, not True is False
'''
1. I notice how it's based on purely what you tell the computer to do. If you tell it to do something that is true, it will return true. If you tell it to do something that is false, it will return false, no matter what.
2. I'd say the bool("abc") expression surprised me the most because I didn't know that a non-empty string would be considered true. I thought it would be false because it is not a number or a boolean value.
3. print(4/2 > 1) would return True because 4 divided by 2 is 2, which is greater than 1.
4. print(4/2 < 1) would return False because 4 divided by 2 is 2, which is not less than 1.
'''

#                    --- Operators ---
#Arithmetic Operators
print(10+5) #15, + addition
print(10-5) #5, - subtraction
print(2*4) #8, * multiplication
print(6/3) #2, / division
print(5%2) #1, % modulus (remainder)
print(3**2) #9, ** exponentiation
print(15//2) #7, // floor division
#Comparison Operators
print(5==2) #False, compares 5 to 2 and asks if they are equal
print(10!=10) #False, compares 10 to 10 and asks if they are not equal
print(2<5) #True, compares 2 to 5 and asks if 2 is less than 5
print(12>5) #True, compares 12 to 5 and asks if 12 is greater than 5
print(5<=6) #True, compares 5 to 6 and asks if 5 is less than or equal to 6
print(1>=10) #False, compares 1 to 10 and asks if 1 is greater than or equal to 10
#Assignments Operators
x=5 
x+=5 #10, new.x=previous.x+5
x-=4 #6, new.x=previous.x-4
x*=3 #18, new.x=previous.x*3
'''
1. The operator "and" returns True if both statements are true.
print(6<10 and 10<15) #True
print(6<10 and 10>15) #False
2. The operator "or" returns True if one of the statements is true.
print(6<10 or 10<5) #True
print(6>10 or 10<5) #False
3. The operator "not" reverses the result, returning False if the result is true and True if the result is false.
print(not(6<10)) #False
print(not(6>10)) #True
'''
'''
1. The difference between / and // is that / returns a float value while // returns an integer value. For example, 5/2 would return 2.5 while 5//2 would return 2.
2. The difference between % and // is that % returns the remainder of a division while // returns the integer value of a division. For example, 5%2 would return 1 while 5//2 would return 2.
3. To calculate the remainder when dividing two numbers, you would use the modulus operator %. For example, 10%3 would return 1 because 10 divided by 3 is 3 with a remainder of 1.
4. Assignment operators are used to assign values to variables. For example, x+=5 is an assignment operator that adds 5 to the current value of x and assigns the result back to x.
'''

#                    --- Strings ---
my_string = "hello"

print(my_string) #hello
print(my_string[0]) #h, prints the first character of the string
print(my_string[1]) #e, prints the second character of the string
print(my_string[2]) #l, prints the third character of the string
print(my_string[3]) #l, prints the fourth character of the string
print(my_string[4]) #o, prints the fifth character of the string
print(my_string[-1]) #o, prints the last character of the string
print(my_string[1:3]) #el, prints the second and third characters of the string
print(my_string[0:5:2]) #hlo, prints every second character of the string
print(len(my_string)) #5, prints the length of the string
print(my_string+ " goodbye") #hello goodbye, adds "goodbye to the string"
print(my_string*7) #hellohellohellohellohellohellohello, repeats the string 7 times
'''
1. Slicing is a way to extract a portion of a string by specifying a start and end index. For example, my_string[1:3] extracts the characters from index 1 to index 2 (not including index 3).
2. name = "Oski"
   print("Hello, my name is", name) 
  This would return "Hello, my name is Oski" because the variable name is linked with the string using a comma.
3. name = "Oski"
   print(f"Hello, my name is {name}")
   This would return "Hello, my name is Oski" because the variable name is linked with the string using an f-string.
4. The difference between using a comma and an f-string is that a comma separates the string and the variable, while an f-string allows you to embed the variable directly into the string.
'''
#                    --- Terminal Commands ---
#Command 1 
'''
cd
Changes directory. Move from one folder to another 
Example: cd Desktop
'''
#Command 2 
'''
ls
Lists all files and directories in the current directory.
Example: ls
'''
#Command 3 
'''
ls -a
Lists all files and directories in the current directory, including hidden files.
Example: ls -a
'''
#Command 4 
'''
mkdir 
Creates a new directory (folder) in the current directory.
Example: mkdir pythondecal
'''
#Command 5 
'''
cat
Displays the contents of a file in the terminal.
Example: cat homework1.py
'''
#Command 6 
'''
pwd
Prints the current working directory (the full path to the current directory).
Example: pwd
'''
#Command 7 
'''
cd ..
Changes directory to the parent directory.
Example: cd ..
'''
#Command 8 
'''
cd .
Changes directory to the current directory.
Example: cd .
'''
#Command 9 
'''
cd ~
Changes directory to the home directory.
Example: cd ~
'''
#Command 10
'''
cp
Copies a file or directory from one location to another.
Example: cp homework1.py homework1_copy.py
'''
#Command 11 
'''
mv
Moves a file or directory from one location to another, or renames a file or directory.
Example: mv homework1.py homework1pythondecal.py
'''
#Command 12 
'''
rm
Removes (deletes) a file or directory.
Example: rm homework1.py
'''
#Command 13 
'''
clear
Clears the terminal screen.
Example: clear
'''
#Command 14
'''
grep
Searches for a specific pattern in a file or output.
Example: grep "hello" homework1.py
'''
'''
1. Three other commands not shown above are: 
   - find: Searches for files and directories based on various criteria.
   - ps: Displays information about running processes.
   - kill: Sends a signal to a process, usually to terminate it.
2. The difference between ls and ls -a is that ls lists only the visible files and directories in the current directory, while ls -a lists all files and directories, including hidden ones (those starting with a dot).
3. A hidden file is a file that is not normally visible when listing the contents of a directory. In Unix-like operating systems, hidden files typically have names that start with a dot (.) and are used for configuration or system purposes. They can be revealed using the ls -a command.
4. Three other flags that can be used with the ls command are:
   - -l: Displays detailed information about files and directories, including permissions, ownership, size, and modification date.
   - -h: Displays file sizes in a human-readable format (e.g., KB, MB, GB) when used with the -l flag.
   - -R: Recursively lists the contents of directories and their subdirectories.
'''