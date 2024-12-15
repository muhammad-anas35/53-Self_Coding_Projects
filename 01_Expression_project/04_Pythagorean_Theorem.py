import math

print("\033[1m Pythagorean Theorem \033[0m")
print("----------------------------\n")

def main():
  try:
    ab : int = int(input("Input First number as value of Ab : "))
    ac : int = int(input("Input Second number as value of Ac : "))

    Solution :int = (ab**2) + (ac**2)
    bc : int = math.sqrt(Solution)
    print(f"The length of BC (the hypotenuse) is:  , {bc:.2f}")
  except ValueError:
    print("Invalid Input")


if __name__ == '__main__':
  main()
