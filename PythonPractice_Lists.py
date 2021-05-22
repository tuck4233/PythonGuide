# -LISTS-


# -You use lists to store multiple sets of variables, you can also cobine different types of variables-
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#             0        1       2       3       4
#            -5       -4      -3      -2      -1

# -The items in the lists have index postions Kevin being 0 and so on-
(friends[0]) # -This would result in only Kevin to be priinted-
(friends[-1]) # -When you use negative numbers it it starts at the back of the list and works it way back-

# -You can also grab items from a lists after a certain index-
(friends[1:]) # -This will grab every item in the list after Kevin-
(friends[1:3]) # -This would grab Karen and Jim-

# -You can also edit lists-
friends[1] = "Mike" # -This would change Kevin to Mike-

# -You can put two lists together by using the extend function_
lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"] 
friends.extend(lucky_numbers) # -This would combine the friends and lucky numbers lits-

#- You can also add on to list with the append function-
friends.append("Creed") # -This would add Creed onto the end of the lists

# -You can add something into a specific spot in a list-
friends.insert(1, "Kelly") # -This would add Kelly after Karen in the lits-

# -You can remove something from a lists-
friends.remove("Jim") # -This removes Jim from the lists-
friends.clear() # -This removes everything inside the lists-
friends.pop() # -This removes the last item within a lists-

# -You can locate an item in the list with index-
friends.index("Oscar") # -This would return 3 as it is the postion of Oscar-
friends.count("Jim") # -This returns the number of times Jim is in the lists, 1-
friends.sort() # -This will sort the list alphebetically or accending order-

# -You can copy a lists-
friends2 = friends.copy() # -This would create a new lists that is a copy of friends-

letters = ['a', 'b', 'c']

print(letters)
  