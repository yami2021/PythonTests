def count_vowel(string, vowels):
    final=[]
    #final = [each for each in string if each in vowels]
    for each in string:
        if each in vowels:
            final.append(each)

    print("The Vowel count in word {} is {}".format(string,len(final)))


string = str(input("Please enter a word"))
vowels = "AaEeIiOoUu"
count_vowel(string, vowels)