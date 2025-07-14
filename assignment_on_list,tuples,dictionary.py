# #assigment 1
# #Create a list of your 5 favorite fruits

# favorite_fruits = ["Mango", "Apple", "Banana", "Grapes", "Orange"]

# #Print the first and last fruit in the list

# print("First fruit:", favorite_fruits[0])
# print("Last fruit:", favorite_fruits[-1])

# #Add a new fruit to the list
# favorite_fruits.append("Pineapple")

# # Remove one fruit from the list
# favorite_fruits.remove("Banana")

# # Print the updated list
# print("Updated fruit list:", favorite_fruits)


# #assignment 2
# #Create a tuple with the names of 4 animals
# animals = ("Lion", "Elephant", "Zebra", "Tiger")

# # Print the second animal in the tuple
# print("Second animal:", animals[1])

# # Try to change one of the animal names
# try:
#     animals[0] = "Leopard"  # This will raise an error
# except TypeError as e:
#     print("Error:",e)

# # # Explain whether tuples can be changed or not
# print("Tuples are immutable, which means you cannot change their elements after creation.")



# #assignment 3
# # Create a dictionary with information about yourself

# my_info = {"name": "Blessed","hobby": "playing games or editing"}

# #Print your name from the dictionary

# print("My name is:", my_info["name"])

# # Add a new key called "favorite_color"
# my_info["favorite_color"] = "Blue"

# # Print the updated dictionary
# print("Updated information:",my_info)


# #assgnment 4
# # List of 3 students
# students = ["Alice", "Brian", "Cindy"]

# # Tuple of 3 subjects
# subjects = ("Math", "Science", "English")

# # Dictionary connecting each student to a subject
# student_preferences = {
#     students[0]: subjects[0],  # Alice likes Math
#     students[1]: subjects[1],  # Brian likes Science
#     students[2]: subjects[2]   # Cindy likes English
# }

# ##Print the dictionary
# print("Student subject preferences:")
# print(student_preferences)

#more exercises on tuples, list and dictionary 


# students = ["Ada", "James", "Fatima", "Chinedu"]

# scores = {
#     "Ada": (85, 90, 88),
#     "James": (78, 75, 80),
#     "Fatima": (92, 88, 95),
#     "Chinedu": (70, 65, 72)}
# top_student = ""
# highest_average = 0

# for student in students:
#     ave_score = sum (scores[student]) / len (scores[student])
#     print(f"{student}'s average score is {ave_score:.2f}")

# if ave_score > highest_average:
#     highest_average = ave_score
#     top_student = student

# print(f"\nThe student with highest average score is{top_student}with an average of {highest_average:.2f}")





inventory = [
    {"name": "Pencil", "price": 20, "quantity": 50},
    {"name": "Notebook", "price": 100, "quantity": 30},
    {"name": "Eraser", "price": 10, "quantity": 100},
    {"name": "Marker", "price": 50, "quantity": 40}
]

most_valuable_item =""
highest_value = 0
total_value = 0 
for item in inventory:
    item_value = item["price"] * item ["quantity"]

total_value += item_value
if item_value > highest_value:
  highest_value = item_value
most_valuable_item = item ["name"]

print(f"total Value of all items: {total_value}")
print(f"most valuable_item is {most_valuable_item} with a value of {highest_value}")


