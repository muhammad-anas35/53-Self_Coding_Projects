print("Ageement BOT")
print("----------------------------\n")

def main():
    user_favorite = input("What's your \033[1m\033[3m Favorite animal \033[0m ? \n")
    user_favorite = user_favorite.title()
    print(f"My favorite animal is also \033[1m\033[3m {user_favorite} \033[0m!")
    print("I hope You Enjoy this .\n")


if __name__ == '__main__':
  main()