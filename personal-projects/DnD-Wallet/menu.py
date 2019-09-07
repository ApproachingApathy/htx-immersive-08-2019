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
        print(value)
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
    print("Input your change in wealth.")
    print("eg. -1g -5c")
    usr_in = input(">> ").lower()
    return usr_in

def convert_to_base(dict_one, value_dict):
    total = 0
    for key in dict_one.keys():
        total += dict_one[key] * value_dict[key]
    return total

def convert_to_highest(int, value_dict):
    total_dict = {}
    for key in value_dict.keys():
        total_dict.update({key:0})
        while int >= value_dict[key]:
            total_dict[key] += 1
            int -= value_dict[key]
    return total_dict

def convert_and_reconvert(dict_one, value_dict):
    return convert_to_highest(convert_to_base(dict_one, value_dict), value_dict)

