from tkinter import *

def odd_or_even(num):
    try:
        int(num)
    
    except:
        print("You didn't input an integer!")

    else:
        if (num % 2 == 0):

            print ("even")
        else:
            print ("odd")

def retrieve():
    return num_entry.get()

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

#keyboard entry
num_entry = Entry(frame, width = 20)
num_entry.insert(0, "Number")

#how to center the entry?
num_entry.pack(padx = 5, pady = 5)

#button that calls function on click
Button = Button(frame, text = "Submit", command = odd_or_even(retrieve))
Button.pack(padx = 5, pady = 5)

root.title("Odd or Even?")
root.mainloop()