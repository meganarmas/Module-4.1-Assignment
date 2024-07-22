# Objective: The aim of this assignment is to 
# enhance your proficiency in using Python modules, 
# both standard and custom, with a specific focus on importing with aliases.

# Task 1: Custom Module with Aliases 

# Problem Statement: Create a custom module named `text_utils.py` 
# with functions for string manipulation (e.g., reversing a string, capitalizing). 
# In your main script, import this module using an alias and utilize its functions.

# Code Example:

    # text_utils.py
    # def reverse_string(s):
        # function to reverse a string

    #def capitalize_string(s):
        # function to capitalize a string

    # main.py
    # Import text_utils using an alias and utilize its functions
# Expected Outcome: 
# Your main script should be able to use the 
# functions from `text_utils.py` via an alias, 
# demonstrating an understanding of custom module creation and aliasing.


import text_utils as tu

def main():
    print("1. Reverse String Function")
    print("2. Capitalizing String Function")
    choice = input("Which would you like to work on? ")

    if choice == '1':
        s = 'testing this'
        reversed = tu.reverse_strings(s)
        print(f"Original: {s} Reversed: {reversed}")
    elif choice == '2':
            s = 'testing this'
            capitalize = tu.capitalizing_strings(s)
            print(f"Original: {s} Capitalized: {capitalize}")
    else:
         print("Wrong number.")

if __name__ == "__main__":
    main()

