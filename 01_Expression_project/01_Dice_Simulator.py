import random 

def Roling_dice():
  dice1 : int = random.randint(1,6)
  dice2 : int = random.randint(1,6)
  return dice1 , dice2

print("\033[1m Dice Simulator \033[0m")
print("----------------------------\n")


def main():
  for i in range(1,4):
    dice1 , dice2= Roling_dice()
    print(f"Rolling {i} \n")
    print(f"Dice1: \"{dice1}\" and Dice2 : \"{dice2}\" \n")



if __name__ == '__main__':
  main()
