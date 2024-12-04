def main():
  try:
   First_number = int(input("Enter first number : "))
   Second_number = int(input("Enter second number : "))
  except ValueError:
    print("Invalid input  ..")

  result = First_number + Second_number
  print(f"Sum of {First_number} and {Second_number} numbers is : {result} ")


if __name__ == "__main__":
  main()
