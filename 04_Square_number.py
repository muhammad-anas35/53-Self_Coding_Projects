print("\033[1m \033[3m Square Number \033[0m")
print("----------------------------\n")


def main():
  try:
    user_input :int = float(input("Enter any number to calculate Square of it : "))
  except ValueError:
    print("Invalid Input")
  else:
    result = user_input ** 2
    print(f"\033[1m Square of {user_input} is {result}\033[0m")



if __name__ == '__main__':
    main()