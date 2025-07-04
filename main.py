from stats import get_num_words
from stats import count_character
from stats import sort_dict_list

def get_book_text(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()
def main():
    # argument parser to get book file path with sys.argv
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file_path = sys.argv[1]
    book_text = get_book_text(book_file_path)
    print(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book_file_path}...")
    num_words = get_num_words(book_text)
    print("---------- Word Count ----------")
    print(f'Found {num_words} total words')
    characters = ['e', 't']
    print("---------- Character Count ----------")
    for character in characters:
        num_character = count_character(book_text, character)
        print(f"'{character}': {num_character}")
    # list of character counts
    character_count = [{'character': c, 'count': count_character(book_text, c)}
                        for c in characters]
    sorted_character_counts = sort_dict_list(character_count, 'count')
    print("---------- Character Count ----------")
    for item in sorted_character_counts:
        print(f"{item['character']}: {item['count']}")
main()





