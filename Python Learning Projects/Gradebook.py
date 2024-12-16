last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#Subjects
subjects = ["physics", "calculus", "poetry", "history"]
#Grades
grades = [98, 97, 85, 88]

#2D list
gradebook = [
  ["Physics", 98], ["Calculus", 97], ["Poetry", 85], ["History", 88]
]
#Commented print function edits have been made
#print (gradebook)

#Adding Science grade
gradebook.append(["Computer Science", 100])
#Commented print function edits have been made
#print (gradebook)

#Adding Visual Arts grade
gradebook.append(["Visual Arts", 93])
#Commented print function edits have been made
#print (gradebook)

gradebook[5][1] = 98
#Commented print function edits have been made
#print (gradebook)

#Switching from a numerical grade value to Pass for poetry
gradebook[2].remove(85)
#Commented print function edits have been made
#print (gradebook)
gradebook[2].append("Pass")
#Commented print function edits have been made
#print (gradebook)

#Adding last_semester_gradebook and gradebook results together
full_gradebook = last_semester_gradebook + gradebook
print (full_gradebook)


