#developer : Faith Ansah
import os

filename = input("Please provide a file name to search and display:\n")

if os.path.exists(filename):
    print("File exists") 

    with open(filename, "r") as f:
        print(f.read())
        f.close()
        
else:
    print("File does not exist")

#command = "cat " + filename
#os.system(command)
