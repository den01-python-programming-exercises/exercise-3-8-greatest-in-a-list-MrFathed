[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5375350&assignment_repo_type=AssignmentRepo)
# Exercise 3.8 Greatest in a list

Write a program that asks the user for strings and adds them to a list. The program stops reading when the user enters -1.

Continue developing the program so that it finds the greatest number in the list and prints its value after reading all the numbers. The programming should work in the following manner.

```plaintext
**72**
**2**
**8**
**93**
**11**
**-1**
The greatest number: 93
```

You can use the source code below as an example. It is used to find the smallest number.

```python
# assume we have a list that contains integers

smallest = list[0]

for i in range(len(list)):
    number = list[i]
    if (smallest > number):
        smallest = number

print("The smallest number: " + str(smallest))
```
