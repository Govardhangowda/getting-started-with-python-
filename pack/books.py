def listbooks():
    """
    Function to list all books in the collection.
    """
    # Assuming we have a list of books stored in a variable called 'books'
    books = [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "1984", "author": "George Orwell"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger"},
        {"title": "Pride and Prejudice", "author": "Jane Austen"}
    ]
    
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}")