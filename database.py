from pymongo import MongoClient

# MongoDB Configuration

def get_db():
    client = MongoClient('mongodb://localhost:27017/')  # Adjust the URI as needed
    db = client['mydatabase']  # Replace with your database name
    return db

# Usage Example
if __name__ == '__main__':
    db = get_db()
    print("Database connected:", db)
