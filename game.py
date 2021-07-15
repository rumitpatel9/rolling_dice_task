import tkinter as tk
from PIL import ImageTk, Image
import random


app = tk.Tk()
app.title("Dice Rolling.")
app.geometry("500x500")
img = ImageTk.PhotoImage(Image.open(f"die{random.randint(1,6)}.PNG"))
panel = tk.Label(image = img)
panel.pack(side = "top", fill = "both", expand = "yes")


def rolling_dice():
	img = ImageTk.PhotoImage(Image.open(f"die{random.randint(1,6)}.PNG"))
	panel.configure(image =img)
	panel.image = img

	
btn = tk.Button(app, text = 'click me.!',command =rolling_dice)
btn.place(x=200, y=400)
app.mainloop()




