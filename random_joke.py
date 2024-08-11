import tkinter as tk
from tkinter import messagebox
import random

# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? Because it was two-tired!"
]

# Function to show a random joke with a visual effect
def show_joke():
    joke = random.choice(jokes)
    joke_label.config(text=joke)
    joke_label.pack(pady=20)
    root.after(100, lambda: joke_label.config(fg="red"))
    root.after(200, lambda: joke_label.config(fg="orange"))
    root.after(300, lambda: joke_label.config(fg="yellow"))
    root.after(400, lambda: joke_label.config(fg="green"))
    root.after(500, lambda: joke_label.config(fg="blue"))
    root.after(600, lambda: joke_label.config(fg="indigo"))
    root.after(700, lambda: joke_label.config(fg="violet"))
    root.after(800, lambda: joke_label.config(fg="black"))

# Create the main window
root = tk.Tk()
root.title("Joke Generator")
root.geometry("400x300")

# Create and pack the joke label
joke_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=350)
joke_label.pack(pady=50)

# Create and pack the button to generate a joke
joke_button = tk.Button(root, text="Tell me a joke!\n 'Click here'", command=show_joke, font=("Helvetica", 16))
joke_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
