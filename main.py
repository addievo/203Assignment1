# Import the operating system module
import os

# This program reads a text file and prints the 10 most common words, the 10 least common words, and the unique words
# that occur only once.

# Define a class named HashMap
class HashMap:
    # Constructor initializes the hash map
    def __init__(self):
        # Set the bucket size (number of buckets)
        self.bucket_size = 10000
        # Initialize each bucket as an empty list
        self.buckets = [[] for _ in range(self.bucket_size)]

    # Define the hash function
    def hash(self, key):
        # Hash the key by summing the ASCII values of its characters, then take the modulo with the bucket size
        return sum(map(ord, key)) % self.bucket_size

    # Define the put method to add a key-value pair to the hash map
    def put(self, key, value):
        # Get the bucket where the key-value pair should be stored
        bucket = self.buckets[self.hash(key)]
        # Iterate over the key-value pairs in the bucket
        for i, (k, v) in enumerate(bucket):
            # If the key already exists, update the value
            if k == key:
                bucket[i] = (key, v + value)
                return
        # If the key does not exist, add a new key-value pair to the bucket
        bucket.append((key, value))

    # Define the get method to retrieve the value associated with a key
    def get(self, key):
        # Get the bucket where the key-value pair should be stored
        bucket = self.buckets[self.hash(key)]
        # Iterate over the key-value pairs in the bucket
        for (k, v) in bucket:
            # If the key is found, return the associated value
            if k == key:
                return v
        # If the key is not found, return None
        return None

    # Define the items method to get all key-value pairs in the hash map
    def items(self):
        # Iterate over all the buckets
        for bucket in self.buckets:
            # Iterate over the key-value pairs in each bucket
            for (key, value) in bucket:
                # Yield each key-value pair
                yield (key, value)

# Define the quicksort function to sort a list of tuples
def quicksort(arr):
    # Base case: if the list has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr
    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]
    # Partition the list into three parts: elements less than, equal to, and greater than the pivot
    left = [x for x in arr if x[1] < pivot[1] or (x[1] == pivot[1] and x[0] < pivot[0])]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x[1] > pivot[1] or (x[1] == pivot[1] and x[0] > pivot[0])]
    # Recursively sort the left and right parts, and concatenate the results
    return quicksort(left) + middle + quicksort(right)

# Define a function to process a word
def process(word):
    # Remove non-alphabetic characters and convert the word to lowercase
    return "".join(c for c in word if c.isalpha()).lower()

# Define a function to get the path to a text file
def get_text_file():
    # Prompt the user for the file path
    file_path = input("Enter the path to your .txt file: ")
    # Remove double quotes from the input, if present
    file_path = file_path.strip('"')
    # Check if the file exists and has a .txt extension
    if not os.path.isfile(file_path) or not file_path.endswith('.txt'):
        # If not, raise a TypeError
        raise TypeError("The path you entered is not for a valid .txt file.")
    # Return the valid file path
    return file_path

# Define the main function
def main():
    # Get the path to the text file
    file_path = get_text_file()
    # Create a HashMap to store word counts
    word_counts = HashMap()

    # Open the text file and read it line by line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into words
            words = line.strip().split()
            for word in words:
                # Process each word
                processed_word = process(word)
                # If the word is not empty, add it to the hash map
                if processed_word:
                    word_counts.put(processed_word, 1)

    # Sort the words by their counts in ascending order
    sorted_words = quicksort(list(word_counts.items()))

    # Print the 10 most common words
    print("The 10 most common words are:")
    for word, count in sorted_words[-10:]:
        print(f"{word}: {count}")

    # Print the 10 least common words
    print("\nThe 10 least common words are:")
    for word, count in sorted_words[:10]:
        print(f"{word}: {count}")

    # Print the unique words that occur only once
    print("\nThe unique words that occur only once:")
    for word, count in sorted_words:
        if count == 1:
            print(f"{word}: {count}")

# Execute the main function if the script is run as a standalone program
if __name__ == '__main__':
    main()
