from pymongo import MongoClient

class DatabaseConnection:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="library_db"):
        """Initialize MongoDB connection"""
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        """Retrieve a specific collection from the database"""
        return self.db[collection_name]

    def insert_document(self, collection_name, document):
        """Insert a document into the specified collection"""
        collection = self.get_collection(collection_name)
        return collection.insert_one(document).inserted_id

    def find_documents(self, collection_name, query={}):
        """Retrieve documents from a collection"""
        collection = self.get_collection(collection_name)
        return list(collection.find(query))

    def close_connection(self):
        """Close the database connection"""
        self.client.close()

# Example Usage
if __name__ == "__main__":
    db = DatabaseConnection()
    books_collection = db.get_collection("books")

    # Insert a test book
    book_data = {"title": "Python Programming", "author": "John Doe", "year": 2024}
    book_id = db.insert_document("books", book_data)
    print(f"Inserted Book ID: {book_id}")

    # Retrieve all books
    books = db.find_documents("books")
    for book in books:
        print(book)

    # Close the connection
    db.close_connection()