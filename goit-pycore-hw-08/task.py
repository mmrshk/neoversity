import os
import pickle

from bot import AddressBook, main as run_bot

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def save_data(book, filename="addressbook.pkl"):
    filepath = os.path.join(SCRIPT_DIR, filename)

    with open(filepath, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    filepath = os.path.join(SCRIPT_DIR, filename)
    try:
        with open(filepath, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()
    try:
        book = run_bot(book)
    finally:
        save_data(book)


if __name__ == "__main__":
    main()
