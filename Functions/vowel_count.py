def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count

Sentence = "My name is aaryan "
print(count_vowels(Sentence))