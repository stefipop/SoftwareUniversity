from project.user import User
from typing import List, Dict


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}
        self.rented_books: Dict[str: Dict[str: int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            self.rented_books.setdefault(user.username, {})[book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for info in self.rented_books.values():
            if book_name in info:

                return f'The book "{book_name}" is already rented and will be available in {info[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str or None:
        if book_name not in self.rented_books[user.username]:

            return f"{user.username} doesn't have this book in his/her records!"

        del self.rented_books[user.username][book_name]
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
