import functions
from data import *

#Get starting wealth
#Convert to copper.
#Get changes in wealth.
#Display to user.
wallet = functions.startup(copper_values)
wallet = functions.convert_and_reconvert(wallet, copper_values)
functions.print_wallet(wallet)
while True:
    transaction = functions.get_wealth_change()
    transaction = functions.interpret_string_to_dict(transaction, copper_values)
    transaction = functions.validate_dict_to_int(transaction)
    wallet = functions.debit_credit(wallet, transaction, copper_values)
    functions.print_wallet(wallet)



# while True:
#     transaction = functions.get_wealth_change()
#     transaction_dict = functions.interpret_string_to_dict(transaction, wallet)
#     transaction_dict = functions.validate_dict_to_int(transaction_dict)




# new_wallet = functions.interpret_string_to_dict("1g 7e 4c", wallet)
# print(new_wallet)
# int_wallet = functions.validate_dict_to_int(new_wallet)
# print(int_wallet)