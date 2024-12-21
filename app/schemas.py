from schemas import User

def test_user_schema():
    user_data = {
        "username": "john_doe",
        "email": "john_doe@example.com",
        "password": "password123"
    }
    user = User(**user_data)
    assert user.username == "john_doe"
    assert user.email == "john_doe@example.com"
