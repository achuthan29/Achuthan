# command.py

import wordcount

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python command.py <filename>")
    else:
        filename = sys.argv[1]
        word_count_dict = wordcount.word_count(filename)
        for word, count in word_count_dict.items():
            print(f"{word}: {count}")
