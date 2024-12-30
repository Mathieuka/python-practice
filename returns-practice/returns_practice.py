# Doc: https://github.com/dry-python/returns?tab=readme-ov-file#maybe-container
import random

from returns.result import Result, Success, Failure
from returns.pipeline import is_successful
from typing import Optional


class UserNotFoundError:
    def __init__(self, user_id: str):
        self.user_id = user_id

    def message(self) -> str:
        return f"Failed to find user with id {self.user_id}"


class User:
    def __init__(self, id):
        self.name = "Matt"
        self.id = id


def find_user(user_id: str) -> Result["User", str]:
    response: Optional[User] = User("1") if random.random() < 0.5 else None

    if response:
        return Success(response)
    return Failure(UserNotFoundError(user_id).message())


user = find_user("1")

# Imperative way
if is_successful(user):
    print(f"User found: {user.unwrap().id}")
else:
    print(f"Error: {user.failure()}")

# FP Way
user.map(lambda user: print(f"User found: {user.id}")).alt(
    lambda error: print(f"Error: {error}")
)
