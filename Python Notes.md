Python
Python wil execute from the top-down until there is nothing left to run.



str(chosenvariable) - converts the variable "chosenvariable" into a string
print (type(variablehere)) - prints out what type of data type variablehere is 
.randint() - uses the random module to generate a random number from a specified range must "import random"



Comments
# - Usually used to explain what something does in a script, to help other people understand the code.
Can also be used to ignore a line of code to see how a program runs without it e.g Debugging.






Print
print() - To print a message.

Ex:
print("dave") - would display dave






Strings
"dave" would be a string.
'dave' is also a string.



Multi-line Strings
```
 OR """ OR "text \
new line\
new line 2"



Ex:
leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.


print (leaves_of_grass)


Defines a variable "leaves_of_grass" and a short poem/text as a multi-line string and prints it.








Variables
Variables can store values/strings for reuse

Ex:
my_variable =  "My string"
print (my_variable) - this would display My string
We store the "My string" in a variable called "my_variable" and then call that variable.


Variables store the results and not the operations.



Ex:
variable = 1 + 1


The variable stores the result 2 and not 1+1.



We can update variables

Ex:
my_variable =  "My string"
print ("What's longer?")
print (my_variable)
my_variable = "Her string"
print ("What's shorter?")
print (my_variable)


Output:
What's longer?
My string
What's shorter?
Her string
Here we updated the variable from "My string" to "Her string"






Numbers
Numbers can be assigned to a value but they don't have the same requirements, they can be used for math operations.



Ex:
my_variable = 54
my_variable2 = 54.54
print (my_variable)
print (my_variable2)


Would print out the number 54 and 54.54



Floating-point number (float)
floats are a decimal number and can be used to represent fractional quantities.






Calculations
Python converts all integers to floats before performing division.
+ - * /



Ex:
calc = 25 * 68 + 13 / 28
print (calc)


Would print the result of the mathematical operation.




Ex:
quilt_width = 8
quilt_length = 8
print (quilt_width + quilt_length


Would print out 64 because 8x8 = 64
Integer (int)
Integers are whole numbers that have no decimal points.



Exponents
How many times the number will multiply. 6**2 =36 because 6x6, 6**3 =216 because 6x6x6
# 2 to the 10th power, or 1024
print(2 ** 10)



Modulo
Indicated by %, gives the remainder of a division calculation.
# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)


# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)









User Input
We can assign variables with user input, the input() function requires a prompt message from the user.



Ex:
my_variable = input("Do you like food? ")


The program would ask the user "Do you like food? " the user could answer the question "Yes"
the variable would be assigned the string "Yes"





Control Flow
Boolean Expressions
To check if a condition is True or False
True or False are different data types known as a "bool" they are the only bool types.
They are called boolean variables.
Boolean values True or False need to be capitalized and do not have quotation marks (otherwise they are a string)


Boolean Operators
and - and combines two boolean expressions and evaluates as true if both statements are true.

Ex:
if (1 + 1 == 2) and (2 + 2 == 4):
 print("chicken")


IF 1+1 = 2(true) and 2+2=4 (true) then print "chicken"


Ex2:
if (1 + 1 == 3) and (2 + 2 == 4):
 print("chicken")


IF 1+1 = 3(false it doesn't = 3 it equals 2) and 2+2=4 (true) will not print "chicken" because one of the
statements is false


or - or combines two expressions into a larger expression that is true if one of the statements is true.

Ex:
if (1 + 1 == 3) or (2 + 2 == 4):
 print("chicken")


if 1+1 =3 (false because 1+1=2) or 2+2=4(true) is true print "chicken" one statement is true so it will print.


Ex2:
if (1 + 1 == 3) or (2 + 2 == 5):
 print("chicken")


if 1+1=3 (false) or 2+2=5(false) is true print chicken, both statements are false so nothing will be printed.



not - not reverses the boolean value, so if we have a true statement and apply a not operator it will be false.

Ex:
if not (1 + 1 == 2) and not (2 + 2 == 4):
 print("chicken")


If not 1+1=2 (true) and not 2+2=4 (true) then print "chicken"
it will not be printed because of the not operator, both statements are true but not make it not true = false.


Ex2:
if not (1 + 1 == 3) and not (2 + 2 == 5):
 print("chicken")
Both statements are false however because of the not operator = not false they will be True






Relational Operators - sometimes known as comparison operators
Relational Operators compare two values and return true or false based on the operands
Logical Operators - Combine multiple boolean expressions


== - equals to operator



Ex:
5 == 5   # True, because 5 is equal to 5
10 == 5  # False, because 10 is not equal to 5



Ex:
a_var = 5
b_var = 10


a_var == b_var


Ex2:
3 == 4


Would be false because both variables have a different value


!= - negation of the equals to operator

Ex:
a_var = 5
b_var = 10


a_var != b_var


Ex2:
5 != 6


Would be true because both variables have a different value


Relational Operators II
> - greater than
>= - greater than or equal to
< - less than
<= - less than or equal to



Ex:
credits = 100
if credits >= 100:
 print("You have reached 100 credits or more")


Checks IF credits are greater than or equal to 100 and prints the message if true.



Exception:
There are exceptions when comparing different data types (string vs integer)



Ex:
2 + 2 == "4"


Would be false because they are different data types (2+2 is an integer "4" is a string)






If statements
An if statement is used to make decisions in your code. It allows you to execute a certain part of code if true.

Ex:
if 2 == 4 - 2: 
  print("apple")


This would print apple because IF 2 is equal to 4-2(2) then print apple


Ex2:
if 2 == 5 - 2: 
  print("apple")


This would not print apple because IF 2 is equal to 5-2(3) it is not equal so it will be false and not print apple.


Ex3:
user_name = "Dave"


if user_name == "Dave":
  print("Get off my computer Dave!")


This would print "Get off my computer Dave!" because the user_name is Dave which is true so it executes print.





Else statements
Else statements allow us to describe what we want our code to do when certain conditions aren't met.



Ex:
if 1 + 1 == 2
 print("True")
else:
 print("False")


If 1+1=2 then print "True" if 1+1= anything other than 2 then print "False"


Else if statements(elif)
elif statements check if another condition after the previous if statements conditions aren't met



Ex:
print("Thank you for donating")


if donation >= 300:
 print("Donation Bronze")
elif donation >= 500
 print("Donation Silver")
elif donation >= 1000
 print("Donation Gold")
else:
 print("Donation Stone")


If user has donated more than or equal to 300 they will receive donation bronze
If user has donated more than or equal to 500 they will receive donation silver
If user has donated more than or equal to 1000 they will receive donation gold
If user hasn't donated above 300 they will receive donation stone


Ex2:
grade = 86


if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")


Match Statements
Match statements are a control flow statement that executes code based on the value of a variable or expression
Match-case statements are more readable compared to if-elif-else statements. 
Hence, in cases where we must check for many values that an expression or variable can take, 
we should use match-case statements.



Ex:
user_name = "Dave"  
match user_name:  
    case "Dave":  
        print("Get off my computer Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Codecademy":  
        print("Access Granted.")  
    case default:  
        print("Username not recognized.")  


If the user_name variable = "Dave" it will print a message "Get off my computer Dave!"
If the user_name variable = "angela_catlady_87" it will print the message "I know it is you, Dave! Go away!"
If the user_name variable = "Codecademy" it will print a message saying "Access Granted."
If the user_name variable = anything other than these three options it will print a message "Username not recognized"






Lists
A list is a built-in data structure that allows us to work with a collection of data in sequential order
List can contain any data type in Python, integers, floats, booleans, strings etc.
A list doesn't have to contain anything, you can create empty lists.

Ex:
heights = [61, 70, 67, 64]


We create a variable "heights" to store height sizes in a list.
A list begins and ends with square brackets [ ]
Each item is separated by a comma ,
It's good practice to insert a space after each comma. (It will work without the space)


List methods:
.append() - appends something to the end of a list
.remove() - removes the first specified value from a list
.count() - counts the number of occurences in a list
.insert() - inserts an element to a specific index of a list
.pop() - removes an element from a specific index of a list
range() - built-in function to create a sequence of integers
len() - built-in function to get the length of a list
.sort() - built-in function to sort a list - it comes after a list, modifies a current existing list
sorted() - built-in function to sort a list - it comes before a list instead of after, generates new list



List Methods
Methods will follow the form of list_name.method()
Some methods will require an input value that will go between parenthesis ( )


.append()

Ex:
what_to_eat = [ "I", "will", "eat"]
what_to_eat.append("chicken")
print (what_to_eat)


This would print ['I', 'will', 'eat', 'chicken'] we appended chicken to the list.


.remove()
We can remove elements in a list using .remove()

Ex:
what_to_eat = [ "I", "will", "eat", "chicken"]
what_to_eat.remove("chicken")
print (what_to_eat)


This would print ['I', 'will', 'eat'] we removed chicken from the list.


+

Ex:
what_to_eat = [ "I", "will"]
what_to_eat_new = what_to_eat + [ "eat", "chicken"]
print (what_to_eat_new)


This would print ['I', 'will', 'eat', 'chicken'] we started with I will and added a new list to that existing list.









List Elements
We call the location of an element in a list it's index, the first element would have an index of 0, the second 1 etc.



Ex:
list = ["name1", "name2"]


First element "name1" has an index of 0, second element "name2" has an index of 1


We can select single elements ex: selecting the first element from a list by using (listname[0])
You must use an int as the index if you use a float you will receive an error.



Ex:
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four = employees[3]
print(employees[3])


Here we have a list of employees, we create a new variable and assign it the value of the listname[indexnumber] and print that variable


Negative Index
We can use the negative index to select an element in a list, negative works from the end of the list backwards.
-1 would be the last item of the list -2 would be the second from last etc.



Ex:
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four = employees[-3]
print(employees[-3])


This would print Ryan


Modifying List Elements
You can modify a lists element using the index numbers 

Ex:
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries"
print(garden)


We have a list called garden and we will replace "Cauliflower" with "Strawberries"
This will print
['Tomatoes', 'Green Beans', 'Strawberries', 'Grapes']



Adding by index - .insert()
.insert() allows us to add an element to a specific index in a list

Ex:
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")
print(store_line) 


Here we insert "Viktor" into the second index and pushes any existing index to the right/changes current "2" to "3"


Removing by index - pop()
pop() allows us to remove elements at a specific index
Using pop() without specifying an index removes the last element of the list.

Ex:
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
removed_element = store_line.pop()
print(store_line)
print(removed_element)


First we made a variable(removed_element) to see which element we will remove
because we didn't specify an index for pop() it removed the last element in the list (Isabella)
our result would be:
["Karla", "Maxium", "Martim"]
"Isabella"


Ex2:
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.pop(1)
print(store_line)


Here we remove "Maxium" from the list using pop() by specifying index 1
This time we will not see "Maxium" printed because we did not assign pop to a variable and print that variable.



Consecutive lists - range()
.range() takes a single output and generates numbers starting at 0 and ending at the number before the input.
If we wanted to use 0 - 9 we would use range(10), it ends at 9 because that's the number before our input (10)
This function creates a range object, in order to use this object as a list we have to covert it using a list()


With two inputs for range we can create a list that starts at a specified number
range(2, 9) - would start at 2 as specified and go up to 8 because that's the number before our specified number(9)


With three inputs we can create a list that skips numbers
range(2, 9, 2) - would start at 2 and because we specified 2 as our third input the following numbers would be 2 greater:
2, 4, 6, 8



Ex:
my_range = range(10)
print (list(my_range))


Here we create a variable(my_range) and create the range object(range(10)
We then print the range using the list function with our variable we made (list(my_range))



Length - len()
len() shows us the number of items/elements in a list/shows us the length.

Ex:
my_list = [1, 2, 3, 4, 5]
print(len(my_list))


This would give us the result of "5" because there are 5 items in our list.


Ex2:
my_list = [1, 2, 3, 4, 5]
length_list = len(my_list)
print(length_list)


This would give us the same result of "5" but we create a variable stored with the result.



Slicing Lists
If we want to extract only a portion of a list we can use slicing.
We can use index numbers to extract the data we want.
[START:END] The ending part always ends one number before the specified number.
For example: [0:5] would print the indexes 0,1,2,3,4 but not 5 because it always ends one number before.


Ex2:
letters = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = letters[2:4]
print(sliced_list)


Here we create a variable with our slice(letters[2:4]) we choose to extract letters C - D
and print that variable so our result would be : ["c", "d"]


Slicing Lists 2
If we want to select the first X amount of elements of a list we could use list[:X]
Slicing the first amount of elements will end the index number before the specified index.
We can also do this to the last X amount of elements of a list using [-X:]
When we use negative indices it will end at the index number we specify, NOT the number before.
You will notice that the ":" are in different places for each example.
[:X] X would be acting as the END number so it always ends the number before we specify.
[X:] X would be acting as the START number so it always prints the number we specify.
So we can also use [:-X] this would end before the number we specify or [X:] which would print the number we specify


First X Elements 
Ex:
letters = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = letters[:3]
print(sliced_list)


This would print ["a", "b", "c"] which is index 0, 1, 2.


Last X Elements 
Ex:
letters = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = letters[-3:]
print(sliced_list)


This would print ["e", "f", "g"] which is index -1, -2, -3.



Counting in a list - .count()
.count() counts occurrences of an item in a list.
.count() can also count element appearences in a 2D list.



Ex:
numbers = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
count_numbers = numbers.count(4)
print(count_numbers)


Here we count how many occurrences of the number 4 there are as specified in numbers.count(4)
The result would be "5" because the number 4 appears 5 times in the list.


Element Appearances in a 2D list EX2:
numbers = [ [1, 1], [2, 2, 2], [1, 1] ]
count_numbers = numbers.count([1, 1])
print(count_numbers)


Here we count how many occurences of the element "[1, 1]" there are.
The result wuld be "2" because it appears 2 times in our 2D list.





Sorting Lists - .sort()
.sort() can sort a list in numerical(1-5) or alphabetical(A-Z) order.
.sort(reverse=True) can also sort in reverse (Z-A) or (5-1)
.sort does not return any value so it does not need to be assigned to a variable.



Ex:
names = ["Chris", "Dave", "Andy", "Bill"]
names.sort()
print(names)


This would output: ["Andy", "Bill", "Chris", "Dave"]
We sorted the names in alphabetical order.



Sorting Lists2 - sorted()
sorted() comes before a list instead of after ( like .sort() )
sorted() generates a new list rather than modifying an existing one ( like .sort() )
sorted() returns a value so it does need to be assigend to a variable if you want it to remember the result


names = ["Chris", "Dave", "Andy", "Bill"]
sorted_names = sorted(names)
print (names)
print (sorted_names)


Here we made a new sorted list in alphabetical order, NOTE it did not change the original names list.



Tuples
Tuples are a built-in data structure, just like lists tuples can hold a sequence of items
Tuples are more memory efficient than lists, Tuples have a slightly higher time efficiency than lists.
Tuples are immutable(we can't modify elements after creating one)
Tuples are good for when you're working with data that won't need to be changed or updated.


len() - Tells us the amount of items in the list/tuple.
max() - returns the tuples/list maximum value. this requires all values to have the same data types e.g strings, integers
min() - returns the tuples/list minimum value. this requires all values to have the same data types e.g strings, integers
.index() - Tells us what index number the value is in the tuple
.count() - counts how many occurences there are in the tuple



Combining Lists - The Zip Function zip()
zip() allows us to quickly combine associated data-sets without relying on multi-dimensional lists.
The zip() function takes two (or more) lists as inputs and returns an object that contains a list of pairs



Ex:
names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]
names_and_heights = zip(names, heights)
converted_list = list(names_and_heights)
print(converted_list)



Here we have two lists, names and heights. We use the zip function to combine these lists
the output would look strange if we didn't convert it. It looks something like: "<zip object at 0x7f1631e86b48>"
this zip object contains the location of this variable in our memory.
We use the list() function to show our list and we get what we were after
[('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]
Notice that this is not a 2D list, it has been converted into tuples.



Two-Dimensional (2D) Lists
Lists can contain other lists, we refer to these as two-dimensional (2D) lists



Ex:
heights = [
["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]
]
print (heights)


This is the result: [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]


Ex2:
ages = [
  ["Aaron", 15], ["Dhruti", 16]
  ]
print (ages)


This is the result: [['Aaron', 15], ['Dhruti', 16]]



Accessing 2D lists via index
You can use the previous methods with 2D lists but you make a couple changes.



Ex:
heights = [
["Noelle", 61], ["Ali", 70], ["Sam", 67]
]
show_height = heights[0][1]
print (show_height)


Prints 61, we select index 0 which points to ["Noelle", 61] then select the second element of the first element "61"
If we used heights[0][0] it points to the first element again, but selects the first element of the first element "Noelle"


Ex2:
heights = [
["Noelle", 61], ["Ali", 70], ["Sam", 67]
]
show_height = heights[2][1]
print (show_height)


Prints 67, we select index 2 which points to ["Sam", 67] then select the second element within that element "67"



Modifying 2D lists



Ex:
incoming_class = [
  ["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]
  ]


print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)


This would select the third element ["Madison", "Indian", 7] and change the third element "7" to 8



Ex2 Remove:
customer_data = [
  ["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]
  ]
customer_data [1].remove(False)
print (customer_data)


Select customer_data list index 1 ["Ben", "Large", False] and removes ", False" from the list.





Loops
Loops are used to repeatedly execute a block of code. 
Temporary variables name is arbitrary and does not need to be defined before using it.



For loops
Each iteration of a for loop we will perform an action on each element of the collection
Structure 
Ex:
for <temporary variable> in <collection>:
 <action>


"for" indicates the start of a for loop
"<temporary variable>" used to represent the value of the element in the collection the loop is currently on
"in" keyword that separates the temporary variable from the collection used for iteration
"<collection>" to loop over (lists, tuples, strings, dictionaries, sets, ranges, files)
"<action>" to do an action on each iteration of the loop



Ex:
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]


for ingredient in ingredients:
  print(ingredient)


First there is a list with 5 elements linked to the variable "ingredients"
we start a for loop with "for"
we then create the temporary variable "ingredient" and uses the list "ingredients"
prints each ingredient from "ingredients" list on a new line because print() is being used in a loop
it would be like
print("first element")
print("second element")
etc.



for loop with range() ex:
six_numbers = range(6)
# this would create a range of 6 numbers (0-5). 
#0, 1, 2, 3, 4 ,5
for numbers in range(6):
 print("Loop is on iteration number " + str(numbers + 1))
 #We are adding +1 to each iteration number because we want to see it start as 1 instead of 0 when it prints.


Output would be
Loop is on iteration number 1
Loop is on iteration number 2
Loop is on iteration number 3
Loop is on iteration number 4
Loop is on iteration number 5
Loop is on iteration number 6



Ex2:
promise = "I will finish the python loops module!"
for promises in range(5):
  print(promise)


First we created a variable "promise" with a string
We create our for loop with the temp variable "promises" and create a range of numbers(0,1,2,3,4) 5 numbers.
Finally, we print the value of promise which would display the string 5 times.






While loops
A while loop performs a set of instructions as long as a given condition is true.
Indefinite iteration


Structure:
while <conditional statement>:
#Loop body begins
 <action>



Ex:
count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1


Elegant 
Ex:
count = 0
while count <= 3: print(count); count += 1


variable "count" is assigned the value of "0"
while loop starts and checks if the variable "count" is less than or equal to "3"
It is less than 3 so the loop body executes
in the loop body the count is printed and then incremented by 1
The first iteration of the loop will finish and will return to the top of the loop and check the condition again
now count would be = 1 again the condition is true so it would iterate again this will repeat until the condition is false
which would happen when count = 4 because 4 is not less than 3 or equal to 3.



Ex2:
countdown = 10
print("Starting While Loop")
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")



While Loops - Lists



Ex:
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
length = len(ingredients)
index = 0


while index < length:
  print(ingredients[index])
  index += 1


variable "ingredients" has a list with 5 elements
variable "length" value is the length of the ingredients list (5 elements)
variable "index" starting at 0
while loop checks if "index" (0) is less than "length" (5)
if true print from list ingredients element 0 (milk)
increment index by 1 (1)
next iteration
while loop checks if "index" (1) is less than "length" (5)
if true print from list ingredients element 1 (sugar)
increment index by 1 (2)
etc.


Loop Control Statements:
Break - Immediately terminates a loop when certain conditions are met
Continue - Used to skip iterations when certain conditions are met


Loop Control: Break
A break immediately terminates a loop, usually used after a condition has been met



Ex:
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]


print("Checking the sale list!")


for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break


print("End of search!")


prints "Checking the sale list!" before it starts our for loop
Goes through each item in items_on_sale list and checks for a match for "knit dress"
if found the code will perform the break statement which will terminate the loop.
prints "End of search!"



Loop Control: Continue
Continue is used to skip iterations when certain conditions are met.



Ex:
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
  if i <= 0:
    continue
  print(i)


Checks each number in the "big_number_list" if the number is less than 0 or equal to 0 then skip that number
prints all numbers that do not match the conditions.



Nested Loops
A nested loop is a loop inside another loop. This allows us to iterate over multiple sequences (or perform multiple iterations)
within each iteration of the outer loop.



Ex:
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
for team in project_teams:
  for student in team:
    print(student)


project teams is a 2D list with 3 elements and each element has elements inside
there is a for loop that lists the 3 teams within project_teams
we have a nested for loop within the for loop that lists the names of each individual within those teams





List Comprehensions
Provide a concise way to create lists. 
They allow you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or range).
It combines the loop and list creation in a single line of code.


NOT COMPREHENSION EXAMPLE:
numbers = [2, -1, 79, 33, -45]
doubled = []


for number in numbers:
  doubled.append(number * 2)


print(doubled)


Here we have a list "numbers" of integers and we create a list "doubled" where each element has been doubled.
for number(temp variable) in numbers(variable and list we created):
doubled(list we created to hold our doubled numbers) .append(number * 2) .append adds list of numbers multiplied by 2
prints doubled list


COMPREHENSION EXAMPLE:
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)


Here we have a list "numbers" of integers and we create a list "doubled" where each element has been doubled.
new_list = [<expression/temp variable> for <element> in <collection>]
doubled(list) [num(tempvariable) * 2 (multiply by 2) for(loop) num(tempvariable) in numbers(list with integers)



COMPREHENSION EXAMPLE 2:
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [num + 10 for num in grades]
print(grades)
print(scaled_grades)


List Comprehensions: Conditionals
Incorporating conditional logic into a List Comprehension
When an if statement is used without else the conditional must use [expression for <element> in <collection> if condition]
When an if statement is used WITH else the conditional must use [expression_if_true if condition else expression_if_false for <element> in <collection>]
expression: The operation applied to each element that passes the condition. - [tempvariable + 2] is an expression temp variable sum = expression
element: The variable representing each item in the collection.
collection: The iterable (list, range, etc.) you are looping through. - list/touple etc
condition: The condition that filters elements.
if without else
[TEMPVARIABLE * 2 for [TEMPVARIABLE in LIST if 2 == 0]
if with else
[TEMPVARIABLE * 2 if [TEMPVARIABLE % 2 == 0 else [TEMPVARIABLE * 3 for [TEMPVARIABLE in LIST]



Ex:
numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)


Here we have a list "numbers" of integers and we create a list "negative_doubled" where each negative element gets doubled
negative_doubled(list) [num(tempvariable) * 2 (multiply by 2) for(loop) num(tempvariable) in numbers(list with integers) if num(tempvariable) < 0 (is less than 0) 


Explained:
can_ride_coaster = [height for height in heights if height > 161]
the first height is what will be added to the new list
the second height is the temp variable representing each element of the heights(list)





if else condition 
Ex:
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)


Here we have a list "numbers" of integers and we create a list "doubled" that doubles all numbers if the number is less than 0 if not then multiply number by 3
doubled(list) [num * 2 if num < 0 (multiply number by 2 if number is less than 0) else num * 3 for num in numbers (multiply number by 3 if it doesn't match first condition) 



Trying to understand List Comprehension
[hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
Although the list is written like this, Python processes it in another way:


[for i in range(len(new_prices)) if new_prices[i] < 30 hairstyles[i]


As a for loop it would be:
cuts_under_30 = []
for i in range(len(new_prices)): 
    if new_prices[i] < 30:  
        cuts_under_30.append(hairstyles[i])
print(cuts_under_30)



Infinite Loops
A loop that never terminates/ends is called an infinite loop
These are dangerous for our code because they will make our program run forever and consume all of a computers rss(resources)



Functions






Errors:
SyntaxError - There is something wrong with the way your code is written.
Punctuation, missing prenthesis or a command that shouldn't be there.


NameError - When the Python interpreter sees a word it does not recognize.


TypeError - It will tell you, maybe the integer wasn't converted to a string?


ZeroDivisionError - When attempting to divide by 0


IndexError - Calling an index that doesn't exist.


ValueError - Calling a value that doesn't exist?



PRACTICE:


List Comprehensions
