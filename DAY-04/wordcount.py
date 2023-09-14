# wordcount.py

import sys

def word_count(filename):
    try:
        with open("apple.txt", 'r') as file:
            text = file.read()
            words = text.split()
            word_count_dict = {}
            for word in words:
                word = word.lower()
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1

            return word_count_dict
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return {}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wordcount.py <filename>")
    else:
        filename = sys.argv[1]
        word_count_dict = word_count(filename)
        for word, count in word_count_dict.items():
            print(f"{word}: {count}")
