Sec_in_day : int = 24 * 60 * 60

print("\033[1m Seconds in Year \033[0m")
print("----------------------------\n")


def main():
  try:
   Years : int = int(input("Input the Years to Convert into Seconds : ")) 
   Days_in_years : int = Years * 365
   Sec_in_year = Days_in_years * Sec_in_day
   print(f"Number of seconds in {Years} years is {Sec_in_year}")
  except ValueError:
    print("Invalid Input as year")



if __name__ == '__main__':
  main()