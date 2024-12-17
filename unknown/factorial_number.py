print("\033[1m Factorial Number  \033[0m ")
print("----------------------------\n")


def main():
  try:
    number : int = int(input("Enter a number to calculate Factorial : "))
  except ValueError:
    print("Your Input number is Invalid ")
    
  def factorial(number):
    if number == 0:
      return 1
    else:
      return number * factorial(number - 1)

  factorial_result = factorial(number)
  print(f"Factorial of {number} is {factorial_result}")



if __name__ == '__main__':
  main()