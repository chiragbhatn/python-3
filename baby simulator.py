from random import choice
questions = ["why is there face on the moon?: ", "where are dinasaur:","why are you alive?"]
question = choice(quetsions)
answer=input("whyis the sky blue?:")
while answer != "just because":
    answer= input("why?:").strip().lower()
print("okay")
