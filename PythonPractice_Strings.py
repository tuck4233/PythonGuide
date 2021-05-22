# -STRINGS-


# -You can call string and then add to them-
phrase = "Giraffe Academy"
(phrase + " is cool")

# -You can alter a string with commands-
(phrase.lower()) # Makes string all lower case
(phrase.upper()) # Makes string all upper case

# -You can also check if a string is upper case or lower case, it will respond with True or False-
(phrase.isupper())
(phrase.islower())

# -You can combine these-
(phrase.upper().isupper()) # -We will then get a True back-

# -You can check the length of a line by using this command-
(len(phrase))

# -In a string you can also grab a character-
(phrase[0]) # -When this is run it will come back with 'G' as it is the first chararcter in the string-

# -You can locate the location of a character with index-
(phrase.index("G")) # -It will come back with the location of G in the string-

# -You can replace a charcter in a string-
(phrase.replace("Giraffe", "Elephant")) # -Giraffe Academy becomes Elephant Academy-





