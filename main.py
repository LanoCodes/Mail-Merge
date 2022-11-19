import os
# with open("./Input/Names/invited_names.txt", mode="r") as invitees_file:
#     invitees = invitees_file.readlines()

with open("./Input/Names/some_ceos.txt", mode="r") as invitees_file:
    invitees = invitees_file.readlines()

# with  open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
#     template = starting_letter.readlines()
#     new_letter_addressee = []

with  open("./Input/Letters/template.txt", mode="r") as starting_letter:
    template = starting_letter.readlines()
    new_letter_addressee = []

for name in invitees:
    name = name.strip()
    # new_letter_addressee.append(template[0].replace("[name],", name + ",").strip())
    new_letter_addressee.append(template[0].replace("[name],", name + ","))

file_name_start = "letter_for_"
file_names = []
for name in invitees:
    # file_names.append(file_name_start+name.strip()+".txt")
    file_names.append(file_name_start + name.strip() + ".txt")
print(file_names)



letter = template.copy()
letters_to_send = []
for index, addressee in enumerate(new_letter_addressee):
    # print(new_letter_addressee[index])
    letter[0] = new_letter_addressee[index]
    letters_to_send.append(letter)
    print(letters_to_send[index])
    with open(os.path.join("/Users/delanopowell/Desktop/100 DoC/Projects/Mail Merge /Output/ReadyToSend", file_names[index]), mode="w") as files:
        # files.write(str(letters_to_send[index]))
        files.write(''.join(letters_to_send[index]))

    # add the above letter to the correct file
    # print(letter)

# test
# print(letters_to_send)


# Backup just in case starting_letter file gets boonswaggled
# Dear [name],
#
# You are invited to my birthday this Saturday.
#
# Hope you can make it!
#
# Angela
