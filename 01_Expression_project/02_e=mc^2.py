c : int = 299792458

print("\033[1m e=mc2 \033[0m")
print("----------------------------\n")



def main():
  try :
    Mass_in_Kg: int = int(input("Enter mass in Kg : "))
    m = Mass_in_Kg
  except ValueError:
    print("Invalid Input")
  else:
    E : int = m*c**2 
    print(f"Energy in Joules is {E} kg")


if __name__ == '__main__':
  main()
