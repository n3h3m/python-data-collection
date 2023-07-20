from typing import List

from models import User


def generate_users() -> List[User]:
    sample_users = [
        User(name="John"),
        User(name="Jane"),
        User(name="Alice"),
        User(name="Bob"),
    ]
    return sample_users
