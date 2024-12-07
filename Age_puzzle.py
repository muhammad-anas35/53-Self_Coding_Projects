print("How_old_are_they")
print("----------------------------\n")

def main():
    Hassan_age = int(input("Input Your age : ")  )

    Ahsan_age : int = Hassan_age + 6
    Rana_age : int = Ahsan_age + 20
    Malik_age : int = Hassan_age + Rana_age
    latif_age : int = Rana_age

    print(f"\nYour_age =  {Hassan_age} \n")
    print(f"Ahsan_age =  {Ahsan_age} \n")
    print(f"Rana_age =  {Rana_age} \n")
    print(f"Malik_age =  {Malik_age} \n")
    print(f"latif_age =  {latif_age} \n")

if __name__ == '__main__':
  main()