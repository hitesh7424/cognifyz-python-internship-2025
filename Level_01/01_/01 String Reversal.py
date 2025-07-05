# Reverse a String

# Prompt the user to enter a string
input_string = input()

# Function to reverse a string using slicing
def string_reverse(string):
    return string[::-1]

# Call the function to reverse the input string
reversed_string = string_reverse(input_string)

# Print the reversed string
print(reversed_string)