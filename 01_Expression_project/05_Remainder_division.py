print("\033[1m Remainder Division \033[0m")
print("----------------------------\n")

def main():
  try:
    dividend : int = int(input("Input Dividend : "))
    divisor : int = int(input("Input Divisor : "))
    remainder : int = dividend % divisor
    print(f"Remainder of ({dividend} by {divisor}) = {remainder}")
  except ValueError:
    print("Invalid Input")


if __name__ == '__main__':
  main() 
