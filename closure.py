#closure is a function having access to the scope of its parent function after the parent function has returned

def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\nperson "+ person + " has " + str(coins) + " coins")
        elif coins == 1:
            print("\nperson "+ person + "has" + str(coins) + " coins")
        else:
            print("no coin left")

    return play_game

tommy = parent_function("Tommy")
jimmy = parent_function("Jimmy")

tommy()
tommy()
tommy()
jimmy()