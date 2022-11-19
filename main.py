import os

with open("./Input/Names/some_ceos.txt", mode="r") as invitees_file:
    invitees = invitees_file.readlines()

with open("./Input/Letters/template.txt", mode="r") as starting_letter:
    template = starting_letter.readlines()
    new_letter_addressee = []

for name in invitees:
    name = name.strip()
    new_letter_addressee.append(template[0].replace("[name],", name + ","))

file_name_start = "letter_for_"
file_names = []
for name in invitees:
    file_names.append(file_name_start + name.strip() + ".txt")

letter = template.copy()
letters_to_send = []
for index, addressee in enumerate(new_letter_addressee):
    letter[0] = new_letter_addressee[index]
    letters_to_send.append(letter)

    with open(os.path.join("/Users/delanopowell/Desktop/100 DoC/Projects/Mail Merge /Output/ReadyToSend", file_names[index]), mode="w") as files:
        files.write(''.join(letters_to_send[index]))