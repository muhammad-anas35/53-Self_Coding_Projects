print("\033[1m Feet to Inches \033[0m")
print("----------------------------\n")

def main():
  try:
    feet : int = float(input("Input Number of Feet : "))
  except ValueError:
    print("Invalid Input")

  inches : int = feet * 12
  print(f"{feet} Feet = {inches} Inches")



if __name__ == '__main__':
  main()