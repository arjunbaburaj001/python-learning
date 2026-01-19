with open("filename.txt", "w") as file:
    file.write("Hello, World!") # Writes a single string (overwrites if file exists)

with open("filename.txt", "w") as file:
    file.writelines(["First Line\n", "Second Line\n", "Third Line\n"])
    # Writes Multiple lines to a file but all in 1 code line

with open("filename.txt", "a") as file:
    file.write("Hello, World!") # This line will be appended at the end of the program