
with open("filename.txt", "mode") as file:
    print("How to open and close a file automatically in 1 line")

with open("filename.txt", "r") as file:
    print("(Default) Read Mode, and reads the file")

with open("filename.txt", "w") as file:
    print("Write Mode, overwrites file if it already exists")

with open("filename.txt", "a") as file:
    print("Append Mode, adds to the end of the file")

with open("filename.txt", "r+") as file:
    print("Read and Write Mode, however file must exist")

with open("filename.txt", "w+") as file:
    print("Write and Read mode, overwrites file if already exists")

with open("filename.txt", "a+") as file:
    print("Append and Read mode, adds towards the end of the file")
