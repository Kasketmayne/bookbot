from stats import get_num_words
from stats import count_character

def get_book_text(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()
def main():
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)
    num_words = get_num_words(book_text)
    print(f'{num_words} words found in the document')
    characters = ['t', 'p', 'c']
    for character in characters:
        num_character = count_character(book_text, character)
        print(f"'{character}': {num_character}")
main()





