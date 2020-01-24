import tkinter as tk

HEIGHT = 700
WIDTH = 800

# - Extremely helpful: https://www.tutorialspoint.com/python/python_gui_programming.htm
# - Video: https://youtu.be/D8-snVfekto


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='blue')
frame.place(relx=0.5, rely=0.1, relwidth = 0.75, relheight=0.1, anchor='n')


root.mainloop()


'''

-Templates
### --- This is a related block of code. This is the beginning of the block. Please only use this block.
### --- This is a related block of code. This is the end of the block. Please only use this block. 
### --- This is a related block of code. This is the beginning of the block. Please only use this block.
### --- This is a related block of code. This is the end of the block. Please only use this block. 
### --- This is a related block of code. This is the beginning of the block. Please only use this block.
### --- This is a related block of code. This is the end of the block. Please only use this block. 
### --- This is a related block of code. This is the beginning of the block. Please only use this block.
### --- This is a related block of code. This is the end of the block. Please only use this block. 



### --- This is a related block of code. This is the beginning of the block. Please only use this block.


button = tk.Button(frame, text="Test Button on left", bg='gray', fg='red') # - Defines the button in the frame, bg grey, fg red.
button.grid(row=0, column=0) # - Places the button on grid with row=0 and column=0

label = tk.Label(frame, text="This is a label in the middle.", bg='orange') # - This defines a label with a orange BG on the frame.
label.grid(row=0, column=1)  # - Places the button on grid with row=0 and column=1

entry = tk.Entry(frame, bg='pink') # - This makes a field that you can enter stuff in on the frame. It's pink.
entry.grid(row=0, column=2) # - Places the entry on grid with row=0 and column=2

button = tk.Button(frame, text="Test Button left (Diagonal)", bg='gray', fg='red') # - Defines the button in the frame, bg grey, fg red.
button.grid(row=1, column=0) # - Places the button on grid with row=1 and column=0

label = tk.Label(frame, text="This is a label in the middle (Diagonal).", bg='orange') # - This defines a label with a orange BG on the frame.
label.grid(row=2, column=1)  # - Places the button on grid with row=2 and column=1

entry = tk.Entry(frame, bg='pink') # - This makes a field that you can enter stuff in on the frame. It's pink.
entry.grid(row=3, column=2) # - Places the entry on grid with row=3 and column=2


### --- This is a related block of code. This is the end of the block. Please only use this block. 



### --- This is a related block of code. This is the beginning of the block. Please only use this block.


button = tk.Button(frame, text="Top left corner", bg='gray', fg='red') # - Defines the button in the frame, bg grey, fg red.
button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25) # - Places a button, relative to the frame, in the top left corner.

label = tk.Label(frame, text="Middle top but flush with label.", bg='orange') # - This defines a label with a orange BG on the frame.
label.place(relx=0.3, rely=0, relwidth=0.45 , relheight=0.25) # - Flush with label with some space to separate.

entry = tk.Entry(frame, bg='pink') # - This makes a field that you can enter stuff in on the frame. It's pink.
entry.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.25) # - Top right corner with some space from the label. also, .8 + .2 = 1 (end of screen)

# - Place is nice and responsive. 


### --- This is a related block of code. This is the end of the block. Please only use this block. 



### --- This is a related block of code. This is the beginning of the block. Please only use this block.


button = tk.Button(frame, text="Test Button", bg='gray', fg='red') # - Defines the button in the frame, bg grey, fg red.
button.pack(side='right', fill='x') # - Places the button on the screen filling x coordinate.

label = tk.Label(frame, text="This is a label on the left.", bg='orange') # - This defines a label with a orange BG on the frame.
label.pack(side='left',fill = 'x') # - This puts the label into play on the left side filling X coordinate.

entry = tk.Entry(frame, bg='pink') # - This makes a field that you can enter stuff in on the frame. It's pink.
entry.pack(side='right', fill = 'y') # - This puts the entry into play on the right side filling y coordiante.

# - Play around with this code to better understand it.


### --- This is a related block of code. This is the end of the block. Please only use this block. 



### --- This is a related block of code. This is the beginning of the block. Please only use this block.


button = tk.Button(root, text="Test Button", bg='gray', fg='red') # - Defines the button in the root, bg grey, fg red.
button.pack(side='right', fill='x') # - Places the button on the screen filling x coordinate.

label = tk.Label(canvas, text="This is a label on the left.", bg='orange') # - This defines a label with a orange BG.
label.pack(side='left',fill = 'x') # - This puts the label into play on the left side filling X coordinate.

entry = tk.Entry(canvas, bg='pink') # - This makes a field that you can enter stuff in. It's pink.
entry.pack(side='right', fill = 'y') # - This puts the entry into play on the right side filling y coordiante.


### --- This is a related block of code. This is the end of the block. Please only use this block. 




### --- This is a related block of code. This is the beginning of the block. Please only use this block.


button = tk.Button(root, text="Test Button", bg='gray', fg='red') # - Defines the button in the root, bg grey, fg red.
button.pack() # - Places the button on the screen.
# - You can put direct color hashes into color places. For example #80c1ff

label = tk.Label(frame, text="This is a label", bg='Yellow') # - This defines a label with a yellow BG.
label.pack() # - This puts the label into play.

entry = tk.Entry(frame, bg='green') # - This makes a field that you can enter stuff in. It's green.
entry.pack() # - This puts the entry into play.

label = tk.Label(frame, text="This is a label on the left.", bg='orange') # - This defines a label with a norange BG.
label.pack(side='left') # - This puts the label into play on the left side.

entry = tk.Entry(frame, bg='pink') # - This makes a field that you can enter stuff in. It's pink.
entry.pack(side='right') # - This puts the entry into play on the right side.


### --- This is a related block of code. This is the end of the block. Please only use this block. 




'''
