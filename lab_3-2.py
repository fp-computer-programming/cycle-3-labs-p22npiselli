# Author: Nolan (AMDG) 9/29/2021

x = int(input("How many points did your team score? "))

if x >= 15:
    print("They won the gold")
elif x >= 12:
    print("They won a silver medal")
elif x < 9:
    print("No medal for you")
else:
    print("They won the bronze")
