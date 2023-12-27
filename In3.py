# Chapter 3 Speeding Along witth Lists and Tuples
# looping through a list 循环遍历列表
# #Define a list of numbers.
# scores=[23,52,24,24,5]
# for score in scores:
#     print(score)
# #seeing whether a list contains an item
# students=["Mark","Amber","Todd","Anita","Sandy"]

# # Is Anita in the list?
# has_Anita= "Anita" in students

# #Is Bob in the list?
# has_Bob= "Bob" in students

# print(has_Anita); print(has_Bob)
# #explanation
# #The in operator already returns a boolean value (True if the name is found, False otherwise).
# #By using has_Anita and has_Bob directly, you're working with the boolean results of the membership checks.
# #Converting those booleans back to strings using bool() is unnecessary and can lead to incorrect results.
# #使用 bool() 将这些布尔值转换回字符串是不必要的，并且可能会导致不正确的结果。

# #create a list of strings (names)
# students=["Mark","Amber","Todd","Anita","Sandy"]
# # add the name Goober in the list
# new_student ="Goober"
# # Add whatever name is in new_student to the list
# students.append(new_student)
# # print the entire lsit
# print(students)
# student_name = "Amanda"
# #Add student_name but only if not already in the list.
# if student_name in students:
#     print(student_name + "already in the list")
# else:
#     students.append(student_name)
#     print(student_name + " added to the list")
#inserting an item into a list
# # Replace listname with the name of your list, position with the position you want to insert the item
# #(for example, 0 to make it the first item, 0 to make it the second item, etc..../and so forth...)
# #listname.insert(position,item)
# #For example, the following code makes Lupe the first item in the list:
# ##create a list of strings (names)
# students = ["Mark","Amber","Todd","Anite","Sandy"]
# student_name = "Lupe"
# # Add student_name but only if not already in the list.
# students.insert(0,student_name)
# #show me the new list
# print(students)
# ## changing an item in a list
# # You can change an item in a list using the = assignment operator just like you do with variables.
# # Make sure you include the index number in square brackets to indicattee which item you want to change.
# #The synntax is listname[index] = newvalue
# #create a list of strings (names).
# students = ["Mark","Amber","Todd","Anite","Sandy"]
# students[3]="Hobart"
# print(students) #['Mark', 'Amber', 'Todd', 'Hobart', 'Sandy']

# #Combining lists
# #If you have two lists to combine into a single list, use the extend() function with the following syntax
# #: original.list.extend(additional_items_list)
# #replace original_list with the name of the list to which you'll be adding new list items.
# #using lists named list1 and list2.
# #After executing list1.extend(list2), the first list contains the items from both lists, as you statement at the end.

# #create two lists of Names.
# list1 = ["Zara","Lupe","Hong","Alberto","Jake"]
# list2 = ["Huey","Dewey","Louie","Nader","Bubba"]

# # Add list2 names to list1.
# list1.extend(list2)

# #Print list 1
# print(list1)

#Removing list items
#Python offers a remove() method so you can remove any value from a list.
#If the item is in the list multiple times, only the first instance of the item will be removed.
#For example, the following code display