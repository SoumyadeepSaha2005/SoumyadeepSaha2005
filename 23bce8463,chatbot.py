from datetime import datetime
a = ""
while("exit" or "bye" not in a):
    a = input("Hey, how can I help you today ? Say exit bye to leave! (Lowercase only please.)")
    if("hello" in a):
        print("Hey! Welcome back!! ")
    elif ("how are you " in a):
        print("I'm good, hope you're doing well too!!")
    elif ("hungry" in a):
        print("grab a snicker, lol! XD")
    elif ("thirsty" in a):
        print("drink some water")
    elif ("i want a girlfriend" in a):
        print("dont worry! you have me  ;)")
    elif ("time" in a):
        print("the time is:",datetime.now())
    elif ("exit" or "bye" in a):
        print("bye have a great day!")
        break
    else:
        print("Sorry, I can't understand you!!")
