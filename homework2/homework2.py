# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
'''
Git is the software used to track scripts, GitHub is an online platform that
hosts tracked code in the cloud, and Git Bash is a Windows application used
to type out Git instructions
'''
# 2) What’s the difference between the terminal and the command line?
'''
The terminal is a program that displays the text interface, while the command
line is the literal text-based environment where you type commands in
'''
# 3) How does Windows PowerShell differ from Git Bash?
'''
They differ in syntax, data handling, and purpose; Powershell passes
objects with structured properties, while Git Bash uses raw text strings
'''
# 4) What’s the difference between Anaconda, conda, and Python?
'''
Python is a programming language, Conda is a tool used to manage that
language's packages and environment, and Anaconda is a massive software
bundle that includes both Python and Conda
'''
# 5) What is VS Code? 
'''
VS Code is a free program that can be used to edit files on your computer and 
run scripts in languages such as Python.
'''
# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
'''
Jupyter Notebook is a web-based interactive computational console that allows
it's user to create documents while blending code, equations, etc. It is 
different from Jupyter Lab because it is a single-document interface meant for 
viewing one file at a time unlike the multi-document development in Lab.
'''
# 7) What does ~/ mean?
'''
It is a shortcut that represents the user's home directory.
'''
# 8) What’s the difference between an absolute path and a relative path?
'''
An absolute path gives the direct address of the file from the root directory,
while a relative path gives the address based on the current folder location
'''
# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
'''
Absolute: /home/orend/Desktop/PythonDecal/course_assignments/homework2
Relative: /OrenDavidi/PythonDecal/course_assignments/homework2
'''
# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
'''
cd ..
'''
# 11) What would rm ./ do in your current directory? (Don’t try it!)
'''
./ represents your current directory, so without a direction, nothing will be removed,
unless you use the -rf recursive flag (I learned that in my Java class)
'''
# 12) What do the following commands do?
# git add
'''
Prepares your changes to be saved   
'''
# git commit
'''
Saves your staged changes to your local history
'''
# git push
'''
Uploads your local commits to a remote server
'''

# 13) What's the difference between "git add ." and "git add <file>"?
'''
git add . scans your entire current directory and adds all new, modified, or 
deleted files to the staging area, while git add <file> stags only the file 
you type, leaving other files untouched
'''
# 14) What do "git status" and "git log -1" do?
'''
git status displays the current state of your repository, while git log -1 
shows the details of the most recent commit
'''
# 15) What’s the difference between cloning a repository and pulling from it?
'''
Cloning downloads a brand-new copy of a repository and sets it up for the first 
time, while pulling updates an already existing repository with new changes
'''
# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
'''
In hw1, there was a variable "3j" that I thought was a string but was actually
a complex, so I was frustrated when I kept getting an error in my output. I ended
up just putting it in quotations to make it a string so the output would be 
cleanly returned. 
'''
# 17) What’s a question you still have? What’s something you’re confused about?
'''
I don't have any specific question just yet. I probably will, though!
'''
# 18) Tell me a fun fact!
'''
There are more stars in the universe than there are grains of sand on Earth. 
'''
# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
print(bool(False or True)) #Prints true because the "or" statement demands the output variable to be true