from tkinter import *
from tkinter import simpledialog

#master
root = Tk()
#pack fits to frame
root.geometry("200x150")

#widgets go in the master, including the main frame itself
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

#within the main frame, we add the label
label = Label(frame, text = "What number are you thinking?")
label.pack()

#keyboard entry - didn't work because the initial value in num_entry will always be Number. Should try simpledialog
# num_entry = Entry(frame, width = 20)
# num_entry.insert(0, "Number")

#simpledialog entry
num_entry = simpledialog.askinteger(title="Choose a Number", prompt="Choose a Number", parent=root)

#this label is where my message containing result will show up, placed within the master
result = Label(root, text = "")
result.pack(pady = 20)

def odd_or_even(num):
    
    # I realized that I didn't need to add in an entirely new window
    # global pop
    # pop = Toplevel(root)
    # pop.title("Result")
    # pop.geometry("250x150")


    try:
        int(num)
    
    except:
        # print("You didn't input an integer!")
        result.config(text="You didn't input an integer!")

    else:
        if (num % 2 == 0):

            result.config(text="Your number is even!")
        else:
            result.config(text="Your number is odd!")

odd_or_even(num_entry)

#how to center the entry?
# num_entry.pack(padx = 5, pady = 5)

#button that calls function on click, lambda passes inputs
# button = Button(frame, text = "Submit", command = lambda: odd_or_even(num_entry.get()))
# button.pack(padx = 5, pady = 5)

root.title("Odd or Even?")
root.mainloop()