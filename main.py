
def main():
    book = get_book_text()
    count = count_words(book)
    print(f"Total words in book: {count}")
    char_dict = count_char(book)
    final_list = sort(char_dict)
    print_report(final_list)

def get_book_text():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return file_contents
def count_words(book):
    count = 0
    words = book.split()
    for i in words:
        count += 1
    return count

def count_char(book):
    char_dict = {}
    for word in book:
        lowercase_word = word.lower()
        if lowercase_word not in char_dict:
            char_dict[lowercase_word] = 1
        else:
            char_dict[lowercase_word] += 1
    return char_dict

def print_report(my_list):
    print("---Begin report of book--- ")
    for item in my_list:
        print(f"The: {item['char']} character was found {item['count']} times")
    print("---End of report---")

def sort_on(dict):
    return dict["count"]

def sort(char_dict):
    my_list = []
    for char, count in char_dict.items():
        if char.isalpha() == False:
            continue
        my_dict = {"char": char, "count": count}
        my_list.append(my_dict)
        my_list.sort(reverse=True, key=sort_on)
    return my_list
        



main()