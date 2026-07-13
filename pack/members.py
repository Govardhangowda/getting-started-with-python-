def listmembers():
    members = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Charlie", "email": "charlie@example.com"}
    ]

    for member in members:
        print(f"Name: {member['name']}, Email: {member['email']}")  