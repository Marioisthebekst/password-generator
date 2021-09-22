import random
from tkinter import *

alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', "%", '^', "&", "*", "-", "<", ">", ",", ".", "/", '?', "'", ]

WIN = Tk()
WIN.title("Password Generator")


def generate():
    output.delete(0, 'end')
    password = []
    for position in range(9):
        if position % 3 != 0:
            if random.randint(1, 3) == 1:
                password.append(random.choice(alphabet_lower))
            else:
                password.append(random.choice(alphabet_upper))
        else:
            if random.randint(1, 3) == 1:
                password.append(random.choice(nums))
            else:
                password.append(random.choice(special_characters))
    output.insert(0, ''.join(password))


lbl = Label(WIN, text="Password Generator")
lbl.pack()

button_yes = Button(WIN, text="Generate", bg="#cce3e6", fg="black", command=generate)
button_yes.pack()

output = Entry(WIN)
output.pack()

WIN.geometry("500x250")
WIN.mainloop()