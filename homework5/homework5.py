# ----  Vocabulary Review  ----
''' Git vs. GitHub'''
# Git is software for tracking changes in source code during software development.
# GitHub is a web-based platform that uses Git for version control and collaboration

''' Terminal vs. Command Line'''
# The terminal is a text-based interface for interacting with the operating system.
# The command line is the space within the terminal where commands are typed

''' Local vs. Remote Repositories'''
# A local repository is a version-controlled directory on your own computer.
# A remote repository is a version-controlled directory hosted on a server, like GitHub

''' Version Control'''
# Version control is the practice of tracking and managing changes to software code.

''' Staging Area '''
# The staging area is where changes are prepared before being committed to the repository

''' git add '''
# The git add command is used to add changes in the working directory to the staging area

'''git commit '''
# The git commit command is used to save changes from the staging area to the local repository

''' git push '''
# The git push command is used to upload local repository content to a remote repository.

''' git pull '''
# The git pull command is used to fetch and integrate changes from a remote repository into the local repository

''' pwd '''
# The pwd command is used to print the current working directory and the path to it

''' ls '''
# The ls command is used to list the files and directories in the current working directory

''' cd '''
# The cd command is used to change the current working directory

''' nano '''
# The nano command is used to open the nano text editor to create or edit files

''' touch '''
# The touch command is used to create a new empty file

''' mv '''
# The mv command is used to move or rename files and directories

''' rm '''
# The rm command is used to remove files and directories

''' cat '''
# The cat command is used to display the contents of a file

# ----  A Directory Tree  ----
'''
1. pwd
2. ls
3. cd brianna_repo
4. mv homework5.py homework/
5. cd homework
6. nano homework5.py
7. git add .
   git commit -m "done with hw5"
   git push origin main
8. git pull origin main
   This error occurs if there are changes in the remote repository that are not in the local repository
9. cd ~/Recent/
'''

# Data Types 
def checkDataType(value):
    return type(value).__name__
# Conditionals 
def evenOrOdd(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
# Loops
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Lists 
def duplicateElements(n):
    result = []
    for item in n:
        result.append(item)
        result.append(item)
    return result
# Debugging 
def square(num):
    return num * num

print(square(5))