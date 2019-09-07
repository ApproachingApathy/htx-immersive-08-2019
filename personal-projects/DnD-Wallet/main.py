import menu

#Get starting wealth
#Convert to copper.
#Get changes in wealth.
#Display to user.
wallet = {
    "p":0,
    "g":0,
    "e":0,
    "s":0,
    "c":7000
}

copper_values = {
    "p":1000,
    "g":100,
    "e":50,
    "s":10,
    "c":1
}

starting_wealth = menu.get_starting_wealth()
starting_wealth_dict = menu.interpret_string_to_dict(starting_wealth, wallet)
starting_wealth_dict = menu.validate_dict_to_int(starting_wealth_dict)
starting_wealth_dict = menu.convert_and_reconvert(starting_wealth_dict, copper_values)
print(starting_wealth_dict)


# while True:
#     transaction = menu.get_wealth_change()
#     transaction_dict = menu.interpret_string_to_dict(transaction, wallet)
#     transaction_dict = menu.validate_dict_to_int(transaction_dict)




# new_wallet = menu.interpret_string_to_dict("1g 7e 4c", wallet)
# print(new_wallet)
# int_wallet = menu.validate_dict_to_int(new_wallet)
# print(int_wallet)