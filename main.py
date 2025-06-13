def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return(file_contents)

from stats import word_count
from stats import alpha_count


def main():
    
#    text_output = get_book_text("./books/frankenstein.txt")
#    print(text_output)

#    how_many_words = word_count("./books/frankenstein.txt")    
#    print(f'{how_many_words} words found in the document')

    alphabet = alpha_count("./books/frankenstein.txt")
    print(alphabet)

main()
