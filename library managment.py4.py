# creates reusable function
def show_heading(): # def means define a function
    print("skillcircle library management") 

#list of dictionaries, each book is a dictionary with 6 keys
# 6 keys - number, title, author, intro, borrow_price_per_day and buy_price
books = [
    {
        "number": 1, # key-value, key-value all the way
        "title": "Python Programming",
        "author": "Guido van Rossum",
        "intro": ("An introductory book on Python programming language, covering basics to advanced techniques including data structures, functions, modules, and working with data."),
        "borrow_price_per_day": 5,
        "buy_price": 500
    },
    {
        "number": 2,
        "title": "GitHub for Developers",
        "author": "Chris Wanstrath",
        "intro": ("A practical guide to using GitHub for version control, collaboration, and project management in software development, with tips for best practices and workflows."),
        "borrow_price_per_day": 7,
        "buy_price": 600
    },
    {
        "number": 3,
        "title": "Personality Development for Interviews",
        "author": "John Doe",
        "intro": ("A comprehensive guide to develop confidence, communication skills, and interpersonal qualities essential for technical and HR interviews."),
        "borrow_price_per_day": 4,
        "buy_price": 400
    },
    {
        "number": 4,
        "title": "Excel for Data Analysis",
        "author": "Jane Smith",
        "intro": ("Learn Excel formulas, pivot tables, dashboards, and data visualization techniques to analyze and interpret data effectively."),
        "borrow_price_per_day": 6,
        "buy_price": 550
    },
    {
        "number": 5,
        "title": "Power BI Tools",
        "author": "Mike Johnson",
        "intro": ("Explore Microsoft's Power BI suite for data visualization, reporting, and dashboard creation with real-world case studies."),
        "borrow_price_per_day": 6,
        "buy_price": 600
    },
    {
        "number": 6,
        "title": "Machine Learning Basics",
        "author": "Tom Mitchell",
        "intro": ("An introduction to machine learning concepts, including supervised and unsupervised learning, evaluation metrics, and practical applications."),
        "borrow_price_per_day": 8,
        "buy_price": 700
    },
    {
        "number": 7,
        "title": "Deep Learning with Python",
        "author": "François Chollet",
        "intro": ("Learn deep learning fundamentals using Python and Keras, covering neural networks, CNNs, RNNs, and model deployment."),
        "borrow_price_per_day": 9,
        "buy_price": 800
    },
    {
        "number": 8,
        "title": "Large Language Models Explained",
        "author": "AI Research Team",
        "intro": ("An overview of large language models, architectures, training techniques, and emerging applications in NLP and AI."),
        "borrow_price_per_day": 10,
        "buy_price": 900
    }
]

# global total bill payment for this visit
total_bill = 0

def show_book_menu(): # another function
    print("please select a book for the subject you want:")
    for book in books: # loop for each dictionary inside the 
        print(f"{book['number']} {book['title']} - {book['author']}")
        # use double or single quotes but be consistent 

def get_book_choice(): # yet another function
    while True: # keep asking until the user gives valid input 
        choice = input("enter your choice (number): ")
        if choice.isdigit(): # to check if input is number and contains only digits 
            choice = int(choice)# converts the string to number 
            if 1 <= choice <= len(books): #to ensure range from 1 to the number of books available (8 in this case)
                return choice
        print(f"invalid input.... please enter a number between 1 and {len(books)}")

def show_book_details(choice):
    book = books[choice - 1]
    # f strings display all book data, inside f string you can put {} variables inside and python will replace them with the values
    print(f"book {book['number']}: {book['title']}") # single quotes for dictionary keys,because
                                                     # if used double quotes it would break the string 
    print(f"author: {book['author']}")             
    print("introduction")
    print(book['intro'])
    print("prices:")
    print(f"borrow: {book['borrow_price_per_day']} rupees per day")
    print(f"buy: {book['buy_price']} outright")

#for payment calculations
def purchase_or_borrow(choice):
    global total_bill # to modify the gobal variable
    book = books[choice-1]
    while True:
        print("1 - borrow the book")
        print("2 - buy the book")
        action = input("enter 1 or 2")
        if action == "1":
            days = input("enter number of days to borrow")
            if days.isdigit() and int(days) > 0: # to check if the user enetered a positive integer 
                days_int = int(days)               # convert to integer
                total_cost = days_int * book["borrow_price_per_day"]
                print(f"total borrow cost {total_cost} rupees")
                total_bill += total_cost           # add this to running total bill
                break
            else:
                print("please enter a valid positive number for days")
        elif action == "2":
            print(f"you have chosen to buy '{book['title']}' for {book['buy_price']} price")
            total_bill += book["buy_price"]        # add buying prices to total bill
            break
        else:
            print("invalid input, please enter 1 or 2")

#to ask if user wants to continue
def ask_continue():
    while True:
        print("type 1 to choose another book")
        print("type 2 to exit")
        choice = input("enter 1 or 2")
        if choice in ("1","2"): # to check if input is exactly 1 or 2 
            return choice
        print("invalid input, please enter 1 or 2")

def main():
    show_heading() # title
    while True: # infinite loop
        show_book_menu() # show menu
        choice = get_book_choice() # for valid choice
        show_book_details(choice) # show details
        purchase_or_borrow(choice) # handle payments
        next_step = ask_continue() # ask to continue
        if next_step == "2": # finally the exit condition
            print(f"your total bill is {total_bill} rupees")
            while True:
                paid = input("please pay the total bill amount to exit: ")
                if paid.isdigit() and int(paid) == total_bill:
                    print("thank you for visiting skillcircle library")
                    return
                else:
                    print("amount does not match total bill, please pay exact amount")

#to start the program
main()
