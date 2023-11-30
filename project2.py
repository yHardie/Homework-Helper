# Initialization 
import math
from datetime import datetime, timedelta 

# Dictionary to store homework 
# list to store classes
homework_dict = {}
classes = []

#Introduction
print()
print("Hello! Welcome to Homework Scheduler!")
print()

# Function to add task to homework dictionary

def add_task(class_name, task, time_needed):
    
    # check if class name is in dictionary
    if class_name in homework_dict:
        homework_dict[class_name].append((task, time_needed))
    
    else:
        homework_dict[class_name] = [(task, time_needed)]
 
# Make a list of your classes that have homework 
        
class1 = input("What classes do you have homework for? Please use commas to seperate them. ")

class1 = class1.split(",")

for i in class1:
    classes.append(i.strip()) # strip removes leading space (just in case there are spaces)

# Add homeworks for each class to dictionary

for i in range(len(classes)):
    homework = input("What homework do you have for " + str(classes[i]) + "?")
    hwtime = int(input("How long will it take you to complete this homework? (in minutes)"))
    
    if hwtime == 0:
        print()
        print("You have no homework for " + str(classes[i]) + ".")
        print()
        
    elif hwtime > 0:
        add_task(classes[i], homework, hwtime)

if all(hwtime == 0 for hwtime in [task[1] for tasks in homework_dict.values() for task in tasks]):
    print("You have no homework today!")
    exit()

# Calculate the time per assignment
total_time = 240 # Minutes of study hall 
num_assignments = sum(len(tasks) for tasks in homework_dict.values()) # Number of assignments
time_per_assignment = math.floor(total_time/num_assignments) # Time per assignment

# Generate and print the schedules
start_time = datetime.strptime("7:30", "%H:%M")
current_time = start_time


print()
print("-------------------------------------------")
print("Your Homework Schedule for Today is: ")

for course, tasks in homework_dict.items():
    print()
    print(course + ":")
    print()
    for task in tasks:
        print(current_time.strftime("%H:%M") + " - " + (current_time + timedelta(minutes=time_per_assignment)).strftime("%H:%M") + ": " + task[0])
        current_time += timedelta(minutes=time_per_assignment)