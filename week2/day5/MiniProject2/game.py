import random

class Game:
    def __init__(self):
        self.results = []

    def get_user_item(self):
        while True:
            users_item = input("Select (r)ock, (p)aper or (s)cissors : ")
            if users_item in ["r", "p", "s"]:
                return users_item
            elif users_item == "q":
                return "q"
            else:
                print("\n === You have to enter (r)ock, (p)aper or (s)cissors. ===\n")
        
    def get_computer_item(self):
        computer_item = random.choice("rps")
        return computer_item

    def get_game_result(self):
        useritem = self.get_user_item()
        
        if useritem == "q": # q is detected, we stop the game
            print("\n=== Game aborted ===")
            return "q"
        
        print(f"\nYou choose : {useritem}")

        computer_item = self.get_computer_item()
        print(f"The computer choose : {computer_item}")

        
        if useritem == computer_item :
            result = "draw"
        elif (useritem == "r" and computer_item == "s") or \
            (useritem == "p" and computer_item == "r") or \
            (useritem == "s" and computer_item == "p"):
            result = "win"
        else:
            result = "loss"
        
        self.result = {
            "user_item" : useritem,
            "computer_item" : computer_item,
            "result" : result
        }
        self.results.append(self.result)

        return result

    def play(self):
        result = self.get_game_result()

        if result == "q":
            return "q" # who will go back up in 'main'
        if result == "win":
            print("You won!")
        elif result == "loss":
            print("You lost!")
        else:
            print("You drew!")
        return self.result
