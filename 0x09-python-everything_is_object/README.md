Resources
Read or watch:

9.10. Objects and values
9.11. Aliasing
Immutable vs mutable types
Mutation (Only this chapter)
9.12. Cloning lists
Python tuples: immutable but potentially changing

Tasks
0. Who am I?
mandatory
What function would you use to get the type of an object?

Write the name of the function in the file, without ().

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 0-answer.txt
   
1. Where are you?
mandatory
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 1-answer.txt
   
2. Right count
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 2-answer.txt
   
3. Right count =
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 3-answer.txt
   
4. Right count =
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 4-answer.txt
   
5. Right count =+
mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 5-answer.txt
   
6. Is equal
mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 6-answer.txt
   
7. Is the same
mandatory
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 7-answer.txt
   
8. Is really equal
mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 8-answer.txt
   
9. Is really the same
mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 9-answer.txt
   
10. And with a list, is it equal
mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 10-answer.txt
   
11. And with a list, is it the same
mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 11-answer.txt
   
12. And with a list, is it really equal
mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 12-answer.txt
   
13. And with a list, is it really the same
mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 13-answer.txt
   
14. List append
mandatory
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 14-answer.txt
   
15. List add
mandatory
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 15-answer.txt
   
16. Integer incrementation
mandatory
What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 16-answer.txt
   
17. List incrementation
mandatory
What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 17-answer.txt
   
18. List assignation
mandatory
What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 18-answer.txt
   
19. Copy a list object
mandatory
Write a function def copy_list(l): that returns a copy of a list.

The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module
guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 
No test cases needed

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 19-copy_list.py
   
20. Tuple or not?
mandatory
a = ()
Is a a tuple? Answer with Yes or No.

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 20-answer.txt
   
21. Tuple or not?
mandatory
a = (1, 2)
Is a a tuple? Answer with Yes or No.

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 21-answer.txt
   
22. Tuple or not?
mandatory
a = (1)
Is a a tuple? Answer with Yes or No.

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 22-answer.txt
   
23. Tuple or not?
mandatory
a = (1, )
Is a a tuple? Answer with Yes or No.

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 23-answer.txt
   
24. Who I am?
mandatory
What does this script print?

a = (1)
b = (1)
a is b
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 24-answer.txt
   
25. Tuple or not
mandatory
What does this script print?

a = (1, 2)
b = (1, 2)
a is b
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 25-answer.txt
   
26. Empty is not empty
mandatory
What does this script print?

a = ()
b = ()
a is b
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 26-answer.txt
   
27. Still the same?
mandatory
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 27-answer.txt
   
28. Same or not?
mandatory
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x09-python-everything_is_object
File: 28-answer.txt
