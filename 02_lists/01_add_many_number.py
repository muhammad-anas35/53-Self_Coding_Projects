sumoflist  : list = [0]
def Sum_numbring():
  return sum(sumoflist)

print("\033[1m Add_many_number \033[0m ")
print("----------------------------\n")


def main():
  while True:
   print("select one from below")
   print("1: For Add number ")
   print("2: Exit")

   Choice : str =  input("Enter your Choice : ")
   if Choice == "1":
    try:
        user_input : int = int(input("Input Number to add in list : "))
        sumoflist.append(user_input)
    except ValueError:
      print("Invalid Input")
   elif Choice == "2":
      break
   else:
     print("Invalid Choice")

  print(f"Sum of list is {Sum_numbring()}")
 

if __name__ == '__main__':
    main()