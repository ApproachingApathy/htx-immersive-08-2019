#ApathyWorks

word = input("Input a word: ").lower()
out = {

}

for letter in word:
    #print(letter)
    if letter in out:
        out[letter] += 1
    else:
        out[letter] = 1
print(out)