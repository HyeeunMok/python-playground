with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file: #modifiy - append
# with open("new_file.txt", mode="w") as file: #write
    file.write("\nIs this working!.")