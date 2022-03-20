films={
    "Kashmiri Files":[18,10],
    "Bachan":[15,10],
    "Finding Dory":[3,5]
    }
while True:
    choice=input("what film would you like to watch?:").strip().title()
    if choice in films:
        age = int(input("how old are you?:").strip())
        if age>= films[choice][0]:

            if films[choice][1]>0:
                print("Enjoy the film!")
                films[choice][1]=films[choice][1]-1
        else:
            print("to young")
        
    else:
        print("we dont have this film....")
    
