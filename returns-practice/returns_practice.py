# Doc: https://github.com/dry-python/returns?tab=readme-ov-file#maybe-container
import random
from returns.result import Result, Success, Failure
from returns.pipeline import is_successful


class UserNotFoundError:
    def __init__(self, id: str):
        self.id = id

    def create(self) -> str:
        return f"Failed to find user with id {self.id}"


class User:
    def __init__(self, id):
        self.name = "Matt"
        self.id = id


def find_user(user_id: str) -> Result["User", str]:
    user = User("1") if random.random() < 0.5 else None

    if user:
        return Success(user)
    return Failure(UserNotFoundError(user_id).create())


response = find_user("1")

# Imperative way
if is_successful(response):
    print(response.unwrap().name)

if not is_successful(response):
    print(response.failure())

# Piping
response.map(lambda user: print(f"User found: {user.id}")).alt(
    lambda error: print(f"Error: {error}")
)
