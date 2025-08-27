# Ask user for their name
# name = input("What's your name? ")

# Remove whitespace from str
# name = name.strip()

# Capitalize user's name
# name = name.capitalize()

# Capitalize each first letter
# name = name.title()

# Remove white space and capitalize
# name = name.strip().title()

# All of it at the same time
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# The default documentation on python for print
# print(*object, sep=' ', end='\n', file=None, flush=False )

# Say hello to user
print("hello, ", end='')
print(first)

# Other way to say hello to user
print("hello,", first, sep=' ')

# Other way to say hello to user
print("hello, " + first)

# Other way
print(f"hello, {first}")

#Notes: you could mix between single and double quotes

# Printing the quote marks
print("hello, \"friend\"")
print('hello, "friend"')

print(f'hello, "{first}"')
