import functions
import data

#Get starting wealth
#Convert to copper.
#Get changes in wealth.
#Display to user.


starting_wealth = functions.get_starting_wealth()
starting_wealth_dict = functions.interpret_string_to_dict(starting_wealth, data.wallet)
starting_wealth_dict = functions.validate_dict_to_int(starting_wealth_dict)
starting_wealth_dict = functions.convert_and_reconvert(starting_wealth_dict, data.copper_values)
print(starting_wealth_dict)


# while True:
#     transaction = functions.get_wealth_change()
#     transaction_dict = functions.interpret_string_to_dict(transaction, wallet)
#     transaction_dict = functions.validate_dict_to_int(transaction_dict)




# new_wallet = functions.interpret_string_to_dict("1g 7e 4c", wallet)
# print(new_wallet)
# int_wallet = functions.validate_dict_to_int(new_wallet)
# print(int_wallet)