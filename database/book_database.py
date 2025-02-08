from pymongo import MongoClient

class BookDatabase:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="Library_db"):  # Match the existing database name
        """Initialize MongoDB connection."""
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["books"]
    def insert_book(self, title, author, year, category, availability, book_cover):
        """Insert a new book into the database."""
        book_data = {
            "title": title,
            "author": author,
            "year": year,
            "category": category,
            "availability": availability,
            "book_cover": book_cover
        }
        return self.collection.insert_one(book_data).inserted_id  # MongoDB generates _id automatically


    def get_all_books(self):
        """Retrieve all books from the database."""
        return list(self.collection.find())

    def find_book(self, query):
        """Find books based on a query."""
        return list(self.collection.find(query))

    def update_book(self, book_id, update_data):
        """Update a book's details in the database."""
        return self.collection.update_one({"_id": book_id}, {"$set": update_data})

    def delete_book(self, book_id):
        """Delete a book from the database."""
        return self.collection.delete_one({"_id": book_id})

    def close_connection(self):
        """Close the database connection."""
        self.client.close()

# Example Usage
if __name__ == "__main__":
    db = BookDatabase()
    
    # Insert a sample book
    book_id = db.insert_book(
        title="Python Basics",
        author="John Doe",
        year=2024,
        category="Programming",
        availability=10,
        book_cover="covers/python_basics.png"
    )
    print(f"Inserted Book ID: {book_id}")
    
    # Retrieve and display all books
    books = db.get_all_books()
    for book in books:
        print(book)
    
    db.close_connection()
