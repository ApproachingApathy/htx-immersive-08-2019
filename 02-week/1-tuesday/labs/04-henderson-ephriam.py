#ApathyWorks

phrase = input("Please enter a sentence or phrase: ").lower()
out = {

}

split_phrase = phrase.split(" ")

for word in split_phrase:
    if word in out:
        out[word] += 1
    else:
        out[word] = 1

print(out)