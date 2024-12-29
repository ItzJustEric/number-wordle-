import random




def start_game():
    lives = 6
    board = 5 * '_'
    print(board)
    random_num = str(random.randint(10000, 99999))
    while lives > 0:
        guess = input("enter a 5 digit number: ")
        if guess == random_num:
            print("you guessed the number correctly")
            break
        elif guess != random_num:
            print(f"your guess was incorrect you have {lives-1} attempts remaining")
            lives -=1
        if lives == 0:
            print(f"you ran out of guesses the number was {random_num} ")
        num_to_list = list(random_num)
        updated_board = ""

        for i in range(len(num_to_list)):
            if guess[i] == num_to_list[i]:
               updated_board += f"\033[92m{guess[i]}\033[00m"


            elif guess[i] in num_to_list:
                updated_board += f"\033[93m{guess[i]}\033[00m"
            else:
                updated_board += guess[i]
        print(updated_board)









start_game()

