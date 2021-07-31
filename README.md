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
