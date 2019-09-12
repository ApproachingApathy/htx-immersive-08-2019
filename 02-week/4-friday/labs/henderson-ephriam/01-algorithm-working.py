names = ["Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Danse",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
"Curie", "Danse", "Preston", "Cait", "Piper", "Maccready", "Strong",
]

def remove_duplicates(list):
    final_list = []
    for value in list:
        if value not in final_list:
            final_list.append(value)
    return final_list

print(remove_duplicates(names))