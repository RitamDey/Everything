from string import ascii_letters as letters

str1 = input("Enter a string: ")


# Make a transaltion table using maketrans; returns a dict
table = str1.maketrans(letters, letters[::-1])


print(str1.translate(table))  # Transalte using table
