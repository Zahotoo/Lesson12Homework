friends = int(input("Please tell me how many friends do you have? "))
chocolate = int(input("Please tell me how many chocolates do you have? "))
givefriends = int(chocolate / friends)
leftover = chocolate % friends

print("You should give", givefriends, "chocolates each friends. ")
print("You will have", leftover, "left. ")