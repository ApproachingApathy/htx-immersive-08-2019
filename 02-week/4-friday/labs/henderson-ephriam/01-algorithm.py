names = ["Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Storng",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
]

def remove_duplicates(list):
    final_list = []
    for value_one in list:
        for value_two in final_list:
            if value_one != value_two:
                final_list.append(value_two)
    return list

#remove_duplicates(names)
print(remove_duplicates(names))