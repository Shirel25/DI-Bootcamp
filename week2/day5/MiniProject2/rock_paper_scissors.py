from game import Game

def get_user_menu_choice():
    print("\n===== Menu =====")
    choice = input("(g) Play a new game\n"
                   "(q) Show scores and exit\n"
                   "choice : ")
      
    return choice

def print_result(results):
    res = {"win" : 0 , "loss" : 0 , "draw" : 0}
    for r in results:
        if r["result"] == "win":
            res["win"] += 1
        elif r["result"] == "loss":
            res["loss"] += 1
        else:
            res["draw"] += 1
    
    print("\n===== Game Results =====")
    return res

def main():
    game = Game()
    choice = get_user_menu_choice()

    while True:
        if choice == 'q':
            print(f"Results : {print_result(game.results)}")
            print("Thank you for playing!")
            break
        elif choice == 'g':
            if game.play() == "q":
                print(f"Results : {print_result(game.results)}")
                print("Thank you for playing!")
                print("\n=== Exiting th game ===")
                break
        else:
            print("\n=== You have to enter (g)ame or (q)uit. ===")    
            
        choice = get_user_menu_choice()

    
if __name__ == "__main__":
    main()