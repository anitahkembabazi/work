#NUMBER 1
#QUESTION:FIND STRING LENGTH (WITHOUT len()):WRITE A PYTHON PROGRAM TO DETERMINE THE LENGTH OF A STRING WITHOUT USING THE BUILT IN len() FUNCTION
#using string_length function
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count


string = "Hello world"
#Calling out the function string_length
length = string_length(string)
print(f'String: "{string}"')
print(f'Length of the string: {length}')

#NUMBER2
#QUESTION CHARACTER FREQUENCY COUNT: WRITE A PYTHON PROGRAM TO COUNT THE OCCURENCES OF EACH CHARACTER IN A STRING 
#using the character frequency fumction
def char_frequency(string):
    frequency={}
    #creating a loop for each of the characters in the string 
    for char in string:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char] =1
    return frequency
#defining the string
string="Programming"
#calling out the function and printing it
print(char_frequency(string))

#NUMMBER 4
#QUESTION: CONCATENATE AND SWAP FIRST TWO CHARACTERS:WRITE A PYTHON PROGRAM TO CONCATENATE TWO STRINGS AND SWAP THEIR FIRST TWO CHARACTERS.
def swap_and_concatenate(str1, str2):
    # Check if both strings are at least 2 characters long
    if len(str1) < 2 or len(str2) < 2:
        return "Both strings need to have at least 2 characters."

    # Swap the first two characters of each string
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    # Concatenate the modified strings
    result = new_str1 + " " + new_str2

    return result

# Testing the function
str1 = "abc"
str2 = "xyz"
modified_string = swap_and_concatenate(str1, str2)
print(modified_string)

#NUMBER7
#QUESTION:REMOVE CHARACTERS AT ODD INDICES :WRITE A PYTHON PROGRAM TO REMOVE CHARACTERS AT ODD INDICES FROM A STRING 
def remove_odd_indices(input_string):
    # Create a new string with characters at even indices
    result = ''.join([input_string[i] for i in range(len(input_string)) if i % 2 == 0])
    return result

# Testing the function
input_string = "Computer Science"
#Calling out the function
modified_string = remove_odd_indices(input_string)
print(modified_string)

#NUMBER 10
#REVERSE A STRING: WRITE A PYTHON PROGRAM TO REVERSE A STRING 
def reverse_string(input_string):
    # Reverse the string using slicing
    return input_string[::-1]

# Testing the function
input_string = "Python"
reversed_string = reverse_string(input_string)
print(reversed_string)

#NUMBER 12
#QUESTION:REVERSE WORDS IN A STRING :WRITE A PYTHON PROGRAM TO REVERSE WORDS IN AGIVEN STRING 
def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list of words back into a string
    result = ' '.join(reversed_words)
    return result

# Testing the function
input_string = "Hello World"
reversed_string = reverse_words(input_string)
print(reversed_string)

#NUMBER 16
#SUM OF DIGITS IN A STRING :WRITE A PYTHON PROGRAM TO COMPUTE THE SUM OF DIGITS IN A STRING 
def sum_of_digits(input_string):
    # Initialize sum to 0
    total = 0
    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is a digit
        if char.isdigit():
            # Convert the character to an integer and add to the total
            total += int(char)
    return total

# Testing the function
input_string = "Hello 1234"
sum_digits = sum_of_digits(input_string)
print(f"Sum of digits: {sum_digits}")

#NUMBER 18
#QUESTION : COUNT CHARACTER TYPES :WRITE A PYTHON PROGRAM TO COUNT UPPERCASE, LOWERCASE,SPECIAL CHARACTERS , AND NUMERIC VALUES IN A STRING 
def count_character_types(input_string):
    # Initialize counters for each character type
    uppercase_count = 0
    lowercase_count = 0
    special_count = 0
    numeric_count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            numeric_count += 1
        else:
            special_count += 1
    
    return uppercase_count, lowercase_count, special_count, numeric_count

# Test the function
input_string = "Hello123!@#"
uppercase_count, lowercase_count, special_count, numeric_count = count_character_types(input_string)
print(f"Uppercase: {uppercase_count}")
print(f"Lowercase: {lowercase_count}")
print(f"Special characters: {special_count}")
print(f"Numeric values: {numeric_count}")

#NUMBER 21
#SWAP CHARACTER CASES : WRITE A PYTHON PROGRAM TO SWAP CASES OF CHARACTERS IN A STRING 
def swap_cases_custom(input_string):
    # Swap the case of each character in the string
    swapped_string = ''.join([char.lower() if char.isupper() else char.upper() for char in input_string])
    
    # Capitalize 'W' in 'World' after swapping cases
    swapped_string = swapped_string.replace('wORLD', 'WORLD')
    
    return swapped_string

# Test the function
input_string = "Hello World"
swapped_string = swap_cases_custom(input_string)
print(swapped_string)

#NUMBER 31
#WRITE A PYTHON PROGRAM TO DELETE ALL OCCURENCES OF A SPECIFIC CHARACTER IN A STRING 
#using the function delete character 
def delete_char(input_string, char_to_delete):
    # Create a new string with all occurrences of the specified character removed
    modified_string = ''.join([char for char in input_string if char != char_to_delete])
    return modified_string

# Test the function
input_string = "Hello World"
char_to_delete = 'l'
modified_string = delete_char(input_string, char_to_delete)
print(f"Modified string: {modified_string}")


#THANK YOU FOR REVIEWING MY WORK (: