class AnagramTest:


        word1 = input("please enter first word")
        word2 = input("please enter second word")

        w1=list(word1)
        w2 = list(word2)
        w1.sort()
        w2.sort()
        if len(w1) == len(w2):
            if w1 == w2:
                print("Its an Anagram")
        else:
            print("Not an Anagram")





