known_users=["Lokesh","Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi! my name is Travis")
    name = input("who are you?: ").strip().capitalize

    if name in known_users:
        print("Hello {}".format(name))
        remove=input("would u like to be removed(y/n)?:").lower()

        if remove == "y":
            
            known_users.remove(name)
        elif remove=="n":
            print("k bye")
            
    else:
        print("i am gonna add u if u want{}".format(name))
        add_me=input("add kardu (y/n)?:").strip().lower()
        if add_me=="y":
            known_user.append(name)
        elif add_me == "n":
            print("k bye")
             
      
