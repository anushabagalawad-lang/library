# Library Management System

book_id = input("Enter Book ID: ")
book_name = input("Enter Book Name: ")
author = input("Enter Author Name: ")
publisher = input("Enter Publisher Name: ")
price = input("Enter Book Price: ")
quantity = input("Enter Book Quantity: ")

# Display book details
print("\n--- Book Details ---")
print("Book ID    :", book_id)
print("Book Name  :", book_name)
print("Author     :", author)
print("Publisher  :", publisher)
print("Price      :", price)
print("Quantity   :", quantity)

# Save details to a file
with open("books.txt", "a") as f:
    f.write(
        f"{book_id}, {book_name}, {author}, "
        f"{publisher}, {price}, {quantity}\n"
    )

print("\nBook details saved successfully!")
