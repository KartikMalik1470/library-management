# 📚 SkillCircle Library Management (Python Console App)

A beginner‑friendly Python program that simulates a small library for data‑science related books.  
Users can select books by subject, read details, choose to **borrow or buy**, and finally **pay the total bill** before exiting.

---

## ✨ Features

- 📖 Menu of 8 books focused on data science and related skills:
  - Python, GitHub, Personality Development, Excel, Power BI, Machine Learning, Deep Learning, LLMs
- 🧱 Clean data structure:
  - List of dictionaries (`books`) to store all book information in one place
- 💰 Two pricing options for every book:
  - Borrow: fixed **price per day** (e.g. ₹5/day)
  - Buy: one‑time **outright price** (e.g. ₹500)
- 🔁 Multiple operations in one session:
  - Borrow or buy as many books as you like
- 🧮 Automatic billing:
  - Keeps a running `total_bill` for the entire visit
  - User **must pay exact total** before exiting
- ✅ Beginner‑friendly input validation:
  - Checks numeric inputs and valid ranges using `.isdigit()` and comparisons

---

## 🧠 How It Works (High Level)

1. **Heading**  
   - `show_heading()` prints the title: `skillcircle library management`.

2. **Book Data**  
   - `books` is a **list of dictionaries**.  
   - Each dictionary stores:
     - `number`, `title`, `author`, `intro`
     - `borrow_price_per_day`
     - `buy_price`

3. **Main Menu Flow**  
   - `show_book_menu()` displays all books with numbers.  
   - `get_book_choice()` asks the user to pick a valid number.  
   - `show_book_details(choice)` shows full info and prices.  
   - `purchase_or_borrow(choice)` lets the user:
     - Borrow → enter days → calculates `days * borrow_price_per_day`  
     - Buy → adds `buy_price`  
     - Updates the global `total_bill` variable.
   - `ask_continue()` lets user choose another book or exit.

4. **Exit & Payment**  
   - When the user chooses to exit:
     - Program prints `your total bill is X rupees`.
     - Asks the user to type the exact amount.  
     - Only exits when the paid amount matches the total bill.

---

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Save the file as, for example: `skillcircle_library.py`.
3. Open a terminal / command prompt in the same folder and run:


Follow the on‑screen instructions to select books, borrow or buy them, and pay the final bill.

---

## 📈 Learning Outcomes

This project is ideal for beginners who want to:

- Practice **functions** and breaking a program into logical parts.
- Work with **lists and dictionaries** to store structured data.
- Use **loops** for menus and repeated input.
- Implement **input validation** for safer programs.
- Understand basic **billing logic** (totals, calculations, and payment).

---

## 👨‍💻 Author

**Kartik Malik**  
Aspiring Data Scientist | Python, ML, Data Tools

