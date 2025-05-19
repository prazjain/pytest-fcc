import requests

database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
}

def get_user_from_db(user_id):
    """
    Simulates a database call to get a user by ID.
    """
    if user_id not in database:
        raise ValueError(f"User with ID {user_id} not found.")
    return database[user_id]

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code != 200:
        raise requests.HTTPError("Failed to fetch users.")
    return response.json()