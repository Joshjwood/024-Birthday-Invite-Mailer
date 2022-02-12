with open("./Input/Names/invited_names.txt", "r") as f:
    names = f.readlines()

for name in range(len(names)):
    names[name] = names[name].strip("\n")

with open("./Input/Letters/starting_letter.txt", "r") as l:
    letters = "".join(l.readlines())
    print(letters)

for name in range(len(names)):
    with open(f"./Output/ReadyToSend/{names[name]}'s letter.txt", mode="w") as file:
        file.write(letters.replace("[name]", names[name]))