"""Create a function that takes in a current mood and return a sentence in the following format:
 "Today, I am feeling {mood}".
However, if no argument is passed,
return "Today, I am feeling neutral"
mood_today("happy") ➞ "Today, I am feeling happy"

mood_today("sad") ➞ "Today, I am feeling sad"

mood_today() ➞ "Today, I am feeling neutral"."""


def mood_today():
    mood = input("what is your mood today")
    if mood =='':
        print("Today, I am feeling Neutral")
    else:
        print("Today, I am feeling {}".format(mood))


mood_today()



