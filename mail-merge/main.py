#To Do: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

save_path = "./Output/ReadyToSend/"
invited_names = []
with open("./Input/Names/invited_names.txt") as name_file:
    for name in name_file:
        invited_names.append(name.strip())

for name in invited_names:
    with open("./Input/Letters/starting_letter.txt") as starting_file:
        for line in starting_file:
            new_line = line.replace("[name]", name)
            with open(f"{save_path}letter_for_{name}.txt", mode="a") as letter_file:
                letter_file.write(new_line)

## Angela's answer:

# PLACEHOLDER = "[name]"
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)