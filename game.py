import tkinter as tk
from PIL import ImageTk, Image
import random
# number =gererate_number()
app = tk.Tk()
app.title("Dice Rolling.")
app.geometry("500x500")
img = ImageTk.PhotoImage(Image.open(f"die{random.randint(1,6)}.PNG"))
panel = tk.Label(image = img)
panel.pack(side = "top", fill = "both", expand = "yes")

def hello():
	print("hello")
	img = ImageTk.PhotoImage(Image.open(f"die{random.randint(1,6)}.PNG"))
	# panel = tk.Label(image = img)
	# panel.pack(side = "top", fill = "both", expand = "yes")
	panel.configure(image =img)
	panel.image = img
	# app.mainloop()
	
btn = tk.Button(app, text = 'click me.!',command =hello)
btn.place(x=200, y=400)
app.mainloop()




