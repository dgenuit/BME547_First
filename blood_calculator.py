def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a Choice")
        print("9 -- Quit")
        choice = int(input("Make a choice:"))
        if choice == 9:
            keep_running = False
    print(choice)
    return choice

interface()