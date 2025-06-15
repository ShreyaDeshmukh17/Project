import tkinter as tk
from tkinter import messagebox
from zxcvbn import zxcvbn
from itertools import product

# -------- Password Strength Checker --------
def check_strength():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    result = zxcvbn(password)
    score_label.config(text=f"Score: {result['score']}/4")
    time_label.config(text=f"Crack Time: {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    feedback_label.config(text="Feedback: " + ', '.join(result['feedback']['suggestions']))

# -------- Leetspeak + Wordlist Generator --------
def leetspeak(word):
    leet_map = {
        'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'],
        'o': ['0'], 's': ['$', '5'], 't': ['7']
    }
    combos = [leet_map.get(c.lower(), [c]) for c in word]
    return set(''.join(w) for w in product(*combos))

def generate_wordlist():
    inputs = [name_entry.get(), pet_entry.get(), date_entry.get()]
    years = ['2023', '2024']
    wordlist = set()

    for word in inputs:
        word = word.strip()
        if word:
            wordlist.add(word)
            for variation in leetspeak(word):
                wordlist.add(variation)
                for year in years:
                    wordlist.add(f"{variation}{year}")
                    wordlist.add(f"{year}{variation}")

    with open("custom_wordlist.txt", "w") as f:
        for item in wordlist:
            f.write(item + "\n")

    messagebox.showinfo("Success", f"Wordlist generated with {len(wordlist)} entries!")

# -------- GUI Layout --------
root = tk.Tk()
root.title("Password Strength & Wordlist Tool")
root.geometry("500x600")
root.resizable(False, False)

# Section: Password Strength Checker
tk.Label(root, text=" Enter Password to Check Strength:", font=('Arial', 12)).pack(pady=5)
password_entry = tk.Entry(root, show='*', width=40)
password_entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_strength, bg="lightblue").pack(pady=5)

score_label = tk.Label(root, text="Score: ", font=('Arial', 10))
score_label.pack()
time_label = tk.Label(root, text="Crack Time: ", font=('Arial', 10))
time_label.pack()
feedback_label = tk.Label(root, text="Feedback: ", wraplength=450, font=('Arial', 10))
feedback_label.pack(pady=10)

tk.Label(root, text="").pack()  # spacer

# Section: Custom Wordlist Generator
tk.Label(root, text=" Generate Custom Wordlist", font=('Arial', 12, 'bold')).pack(pady=5)
tk.Label(root, text="Enter Name:").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=2)

tk.Label(root, text="Enter Pet's Name:").pack()
pet_entry = tk.Entry(root, width=40)
pet_entry.pack(pady=2)

tk.Label(root, text="Enter a Date (e.g. Birth Year):").pack()
date_entry = tk.Entry(root, width=40)
date_entry.pack(pady=2)

tk.Button(root, text="Generate Wordlist", command=generate_wordlist, bg="lightgreen").pack(pady=10)

# Run the GUI loop
root.mainloop()



