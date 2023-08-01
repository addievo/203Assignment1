import os
import string
from collections import defaultdict


def get_text_file():
    file_path = input("Enter the path to your .txt file: ")

    # Remove quotation marks from the path

    file_path = file_path.strip('"')

    if not os.path.isfile(file_path) or not file_path.endswith('.txt'):
        raise TypeError("The path you entered is not for a valid .txt file.")

    return file_path


def read_file(path):
    # Open the file and read the text
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            # Remove the newline character
            yield line


def process_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Add quotation marks to punctuation

    punctuation = string.punctuation + '“”‘’'

    # Remove punctuation
    text = text.translate(str.maketrans('', '', punctuation))

    # Split text into words
    words = text.split()

    return words


def count_words(words):
    # Create a dictionary to store the word count

    word_counts = defaultdict(int)

    # Count the words

    for word in words:
        word_counts[word] += 1

    return word_counts


# Since  we can't use sort(), implementing simple bubble sort to use in sort_words func

def bubble_sort(word_counts):
    items = list(word_counts.items())
    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1] or (items[j][1] == items[j + 1][1] and items[j][0] > items[j + 1][0]):
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


# Sorting words

def sort_words(word_counts):
    return bubble_sort(word_counts)


# Printing the results

def print_words(sorted_words):
    # Printing the first 10 words

    print("The 10 most common words are:")
    for word, count in sorted_words[:10]:
        print(f"{word}: {count}")

    # Printing the last 10 words

    print("\nThe 10 least common words are:")
    for word, count in sorted_words[-10:]:
        print(f"{word}: {count}")


def main():
    # Get the file path from the user
    file_path = get_text_file()

    # Initialize a list to store all the words in the file
    all_words = []

    # Read the file line by line
    for line in read_file(file_path):
        # Process each line and get the words
        words = process_text(line)

        # Add the words to the list of all words
        all_words.extend(words)

    # Count the words
    word_counts = count_words(all_words)

    # Sort the words
    sorted_words = sort_words(word_counts)

    # Print the results
    print_words(sorted_words)


if __name__ == '__main__':
    main()
