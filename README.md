# Project :

# 🔐 Password Strength Analyzer & Custom Wordlist Generator

This project combines two core cybersecurity concepts into one practical tool:

1. *Password Strength Checker*
   Uses the `zxcvbn` library to evaluate password strength based on real-world attack patterns and provides crack time estimates along with useful feedback.

2. *Custom Wordlist Generator*
   Accepts personal keywords (like name, pet, birthdate) and generates a realistic wordlist using common transformations like leetspeak and year combinations. Useful for understanding how attackers build targeted password lists.

### 💻 Features
- Simple and clean *Tkinter GUI*
- No external dependencies except `zxcvbn`
- Outputs a `.txt` wordlist compatible with most password cracking tools
- Educational and practical for cybersecurity learners

### 🔧 How It Works
The tool was built keeping both *usability* and *realistic scenarios* in mind. It simulates how easy it is to generate personal wordlists from known information, while also helping people understand how strong (or weak) their passwords are.

### 📁 Output
- `custom_wordlist.txt` – Automatically generated wordlist from user input.
- GUI interface for both features in a single Python script (`gui_app.py`).

### ⚙️ Tools Used
- Python 3
- Tkinter (for GUI)
- zxcvbn (for password strength)
- itertools (for leetspeak variation logic)


 ⚠️ *Note*: This tool is for educational purposes only — it helped me better understand how simple personal information can be turned into attack vectors and how to defend against them by using stronger passwords.



Feel free to explore the code and run the tool. The GUI makes it pretty easy to follow along even without prior programming knowledge.
