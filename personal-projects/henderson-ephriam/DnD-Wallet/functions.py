import data
import time

def get_starting_wealth():
    print("Input your current wealth.")
    print("eg. 1p 2g 3e 4s 5c")
    usr_in = input(">> ").lower()
    return usr_in
    
def interpret_string_to_dict(str, dict):
    """Takes a string and dictionary, searches the string for keys returns a new dictionary with associated values. """
    split_inputs = str.split()
    for value in split_inputs:
        coin_ident_index = len(value) - 1 #The coin identifier should be the last item in the string. 
        if value[coin_ident_index] in dict.keys():
            extracted_value = value.split(value[coin_ident_index])
            dict[value[coin_ident_index]] = extracted_value[0]
    return dict

def validate_dict_to_int(dict):
    for key, value in dict.items():
        dict[key] = validate_to_int(value)
    return dict
    
def validate_to_int(str):
    try:
        number = int(str)
        return number
    except:
        error_msg("Failed to convert value to integer.")

def add_dicts(dict_one, dict_two):
    new_dict = {}
    for key in dict_one.keys():
        sum_of_values = dict_one[key] + dict_two[key]
        new_dict.update({key: sum_of_values})
    return new_dict

def error_msg(msg):
    print(msg)
    exit(1)

def get_wealth_change():
    """Returns string from user input"""
    print("Input your change in wealth.")
    print("eg. -1g -5c")
    usr_in = input(">> ").lower()
    return usr_in

def convert_to_base(dict_one, value_dict):
    total = 0
    for key in dict_one.keys():
        total += dict_one[key] * value_dict[key]
    print(f"DEBUG: Converting to base. Total: {total}")
    time.sleep(1)
    return total

def convert_to_highest(int, value_dict):
    total_dict = {}
    for key in value_dict.keys():
        total_dict.update({key:0})
        while int >= value_dict[key]:
            print("DEBUG: Converting to highest.")
            print(f"DEBUG: {key}: {int}")
            total_dict[key] += 1
            int -= value_dict[key]
    return total_dict

def convert_and_reconvert(dict_one, value_dict, value_dict_two = False):
    if value_dict_two == False:
        value_dict_two = value_dict
    return convert_to_highest(convert_to_base(dict_one, value_dict), value_dict_two)

def startup(value_dict):
    starting_wealth = get_starting_wealth()
    starting_wealth_dict = interpret_string_to_dict(starting_wealth, data.wallet)
    starting_wealth_dict = validate_dict_to_int(starting_wealth_dict)
    starting_wealth_dict = convert_and_reconvert(starting_wealth_dict, value_dict)
    return starting_wealth_dict

def debit_credit(wallet_dict, transaction_dict, value_dict):
    """Credit or debits. """
    initial_copper = convert_to_base(wallet_dict, value_dict)
    print(f"DEBUG: Initial Copper: {initial_copper}")
    transaction_copper = convert_to_base(transaction_dict, value_dict)
    print(f"DEBUG: Transaction Copper: {transaction_copper}")
    final_copper = initial_copper + transaction_copper
    if final_copper < 0:
        print("You don't have enough money for this!")
        return wallet_dict
    else:
        return convert_to_highest(final_copper, value_dict)

def print_wallet(dict):
    #TODO Make this look better.
    if "p" in dict.keys() and "e" in dict.keys():
        platinum = dict["p"]
        electrum = dict["e"]
    else:
        platinum = 0
        electrum = 0    
    
    gold = dict["g"]
    silver = dict["s"]
    copper = dict["c"]
    print(f"You have {platinum} Platinum, {gold} Gold, {electrum} Electrum, {silver} Silver, and {copper} Copper.")
