# Password Generator

A customizable Python password generator that allows the user to choose which types of characters to include. The program validates input, ensures at least one character from each selected group is included, and generates a fully randomized password of the desired length.

---

## 🔐 Features

- User‑defined password length  
- Input validation to prevent letters or invalid values  
- Choice of character groups:
  - Uppercase letters  
  - Lowercase letters  
  - Numbers  
  - Symbols  
- Ensures at least one character from each selected group  
- Randomized and shuffled final password  

---

## 🧠 How It Works

1. The program asks the user for the desired password length.  
2. It then asks whether to include each character group.  
3. At least one group must be selected; otherwise, the program asks again.  
4. One mandatory character from each chosen group is added.  
5. The remaining characters are randomly selected from all chosen groups.  
6. The final password is shuffled and displayed.

---

## ▶️ How to Run

Make sure you have **Python 3** installed.

Run the script from your terminal:
```
python password_generator.py
```

Follow the instructions shown on the screen.

---

## 📝 Example Output

```
Enter the desired password length: 12
Include uppercase letters? (y/n) y
Include lowercase letters? (y/n) y
Include numbers? (y/n) y
Include symbols? (y/n) n

Generated password: aG9kTq2bFhL3
```

---

## 📚 What I Learned

- Validating user input with `try/except`  
- Working with lists, loops, and conditionals  
- Using `random.choice()` and `random.shuffle()`  
- Ensuring constraints (mandatory characters)  
- Building a complete interactive console tool  

---

## 🚀 Future Improvements

- Add a “no ambiguous characters” mode  
- Add strength evaluation for the generated password  
- Allow generating multiple passwords at once  
- Add a graphical interface (Tkinter)  
- Export passwords to a file  

---
