import sys
from stats import count_words
from stats import count_chars
from stats import sort_char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_counts = count_chars(text)
    sorted_chars = sort_char_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("\n--------- Character Count -------")
    for char_info in sorted_chars:
        if char_info["char"].isalpha():
            print(f"{char_info['char']}: {char_info['count']}")

if __name__ == "__main__":
    main()
