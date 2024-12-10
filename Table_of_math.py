print("\033[1m Table Printing \033[0m")     
print("----------------------------\n")


def main():
  end_point : int = 1 
  try:
    user_number : int = int(input("Enter those numbers whose table you want to print : "))
    end_point : int = int(input("Enter end point of table : "))
  except ValueError:
    print("You Input number or end_point is Invalid 1")
  else:
    end_point += 1

  for i in range(1,end_point):
     print(f"{user_number} * {i} = {user_number * i}")
  


if __name__ == '__main__':
  main()
