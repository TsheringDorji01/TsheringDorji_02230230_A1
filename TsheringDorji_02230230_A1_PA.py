import re
import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum(start, end):
    """Return the sum of all prime numbers in the given range (inclusive)."""
    return sum(n for n in range(start, end + 1) if is_prime(n))

def length_converter(value, unit):
    """Convert meters to feet (M -> F) or feet to meters (F -> M)."""
    conversion_factor = 3.28084
    if unit.upper() == 'M':
        return round(value * conversion_factor, 2)
    elif unit.upper() == 'F':
        return round(value / conversion_factor, 2)
    else:
        raise ValueError("Invalid unit. Use 'M' for meters to feet or 'F' for feet to meters.")

def consonant_counter(text):
    """Count the number of consonants in a given string."""
    return len([char for char in text.lower() if char.isalpha() and char not in "aeiou"])

def min_max_finder(numbers):
    """Find and return the minimum and maximum numbers from a list."""
    return min(numbers), max(numbers)

def is_palindrome(text):
    """Check if a given string is a palindrome, ignoring spaces and case."""
    cleaned_text = re.sub(r'\s+', '', text.lower())
    return cleaned_text == cleaned_text[::-1]

def word_counter(filename):
    """Count occurrences of specific words in a file."""
    word_list = ["the", "was", "and"]
    word_counts = dict.fromkeys(word_list, 0)
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = text.split()
            for word in word_list:
                word_counts[word] = words.count(word)
    except FileNotFoundError:
        print("Error: File not found.")
    return word_counts

def main():
    while True:
        print("""
Select a function:
1. Calculate the sum of prime numbers
2. Convert length units
3. Count consonants in a string
4. Find min and max numbers
5. Check for palindrome
6. Word Counter
0. Exit program
""")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                print("Sum of prime numbers:", prime_sum(start, end))
            except ValueError:
                print("Invalid input. Please enter integers.")

        elif choice == '2':
            try:
                value = float(input("Enter the length value: "))
                unit = input("Enter unit (M for meters to feet, F for feet to meters): ")
                print("Converted length:", length_converter(value, unit))
            except ValueError as e:
                print("Error:", e)

        elif choice == '3':
            text = input("Enter a string: ")
            print("Number of consonants:", consonant_counter(text))

        elif choice == '4':
            try:
                num_count = int(input("How many numbers will you enter? "))
                numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num_count)]
                smallest, largest = min_max_finder(numbers)
                print(f"Smallest: {smallest}, Largest: {largest}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        elif choice == '5':
            text = input("Enter a string: ")
            print("Is palindrome:", is_palindrome(text))

        elif choice == '6':
            filename = input("Enter the filename: ")
            print("Word occurrences:", word_counter(filename))

        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 0-6.")

if __name__ == "__main__":
    main()
