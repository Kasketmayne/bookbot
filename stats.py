def get_num_words(book_text: str) -> int:
    words = book_text.split()
    return len(words)
# create function to count specific character in book text with lowercase
# and uppercase letters treated the same
def count_character(book_text: str, character: str) -> int:
    book_text = book_text.lower()
    character = character.lower()
    return book_text.count(character)
# create function to sort a list of dictionaries by a specific key
def sort_dict_list(dict_list: list, key: str) -> list:
    return sorted(dict_list, key=lambda x: x[key])


