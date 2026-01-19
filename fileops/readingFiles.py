with open("filename.txt", "r") as file:
    content = file.read()
    print(content)
# Reads the entire content of the file

with open("filename.txt", "r") as file:
    line = file.readline() 
    print(line) # Prints first line
    # Read one line at a time

with open("filename.txt", "r") as file:
    lines = file.readlines()
    print(lines) # Prints all lines in a list format
    # Read all lines at once and return as a list