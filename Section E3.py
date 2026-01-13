def count_vowels_consonants(s):
    vowels=0
    consonants=0
    for char in s:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowels+=1
            else:
                consonants+=1
    print("vowels:",vowels)
    print("consonants:",consonants)
s=input("enter a string:")
count_vowels_consonants(s)
