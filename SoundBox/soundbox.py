import tkinter as tk
from playsound import playsound
import threading

def handle_click(path):
	print(path)
	x = threading.Thread(target=playsound, args=(path,))
	x.start()

window = tk.Tk()
window.winfo_toplevel().title("My Mini-JukeBox")

tk.Grid.columnconfigure(window, 0, weight=1)
tk.Grid.rowconfigure(window, 0, weight=1)

frame = tk.Frame(master=window)
frame.grid(row = 0, column = 0, sticky= tk.N + tk.S + tk.E + tk.W)

colors = ["blue", "green", "red", "yellow" ]
audio_path = ["audio1.mp3", "audio2.mp3", "audio3.mp3", "audio4.mp3"]
buttons = []

cpt = 0
for i in range(2):
	tk.Grid.rowconfigure(frame, i, weight=1)
	for j in range(2):
		path = audio_path[cpt]

		tk.Grid.columnconfigure(frame, j, weight=1)
		buttons.append(tk.Button(master = frame, text="Play Me",
			 bg=colors[cpt], fg="black",
			 command = lambda p = path: handle_click(p),
			 highlightthickness=0))
		buttons[cpt].grid(row = i, column = j, sticky = tk.N + tk.S + tk.E + tk.W, padx = 5, pady = 5)
		cpt += 1

window.mainloop()
