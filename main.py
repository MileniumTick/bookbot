path_to_file = 'books/frankenstein.txt'

def sort_dict(dict):
    return dict["num"]

with open(path_to_file) as f:
    file_contents = f.read()

    words = file_contents.lower().split()
    chars = {}

    for word in words:
        for char in word:
            if char.isalpha():
                chars[char] = chars[char] + 1 if char in chars else 1


    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")

    char_list = []

    for char in chars:
        char_list.append({"name": char, "num": chars[char]})

    
    char_list.sort(reverse=True, key=sort_dict)

    for char in char_list:
        print(f"The {char["name"]} character was found {char["num"]} times")

    print("--- End report ---")
