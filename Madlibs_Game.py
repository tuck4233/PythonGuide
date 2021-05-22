print(" ")
print("----------------------")
print("| Roses are 'red'    |")
print("|                    |")
print("| 'Violets' are blue |")
print("|                    |")
print("| I love 'you'       |")
print("----------------------")
print(" ")

print('----------------------------------------------------------------------')
print("Lets play a game where you replace the words in quotation marks above!")
print("   (Make sure to leave a space before you begin typing your answer)   ")
print('----------------------------------------------------------------------')
print("")

line1 = ("----------------------")
line2 = ("|  Roses arered     |")
line3 = ("|                    |")
line4 = ("| Violets are blue  |")
line5 = ("|                    |")
line6 = ("|  I loveyou        |")
line7 = ("----------------------")


New_line2 = input("Pick a new 3 letter color to replace 'red'")
New_line4 = input("Pick a new 7 letter plural noun to replace 'Violets' (Hint- 6 letter word with 's'")
New_line6 = input("Pick a new 3 letter noun to replace 'you'")

print(" ")
print(line1)
print(line2.replace("red", New_line2))
print(line3)
print(line4.replace("Violets", New_line4))
print(line5)
print(line6.replace("you", New_line6))
print(line7)


