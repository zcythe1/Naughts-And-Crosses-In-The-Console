# imports
import collections, os, time
from colorama import Fore

# declaring varibles beforehand

r1 = ['_', '_', '_']
r2 = ['_', '_', '_']
r3 = ['_', '_', '_']
goes = 0
p1 = False

# game loop

while True:
  os.system('clear')
  board = f"""
3 |{r3[0]}|{r3[1]}|{r3[2]}|
2 |{r2[0]}|{r2[1]}|{r2[2]}|
1 |{r1[0]}|{r1[1]}|{r1[2]}|
   1 2 3
"""
  print(board)
  if goes == 9:
    print(Fore.RED + '\nDRAW\n' + Fore.WHITE)
    break
  if p1:
    print("p1's go")
  else:
    print("p2's go")
  p1 = not p1
  if goes == 0:
    x = input("enter the co-ordinates of your go in the format of (1, 3) = 13 .\n")
  else:
    x = input('enter your go co-ordinates.\n')
  go = []
  for i in x:
    go += i
  if p1:
    symbol = 'x'
  else:
    symbol = 'o'
  diagonal1 = [r3[2], r2[1], r1[0]]
  diagonal2 = [r3[0], r2[1], r1[2]]
  column1 = [r3[0], r2[0], r1[0]]
  column2 = [r3[1], r2[1], r1[1]]
  column3 = [r3[2], r2[2], r1[2]]
  lines = [r1, r2, r3, diagonal1, diagonal2, column1, column2, column3]
  go1 = int(x[0])
  go2 = int(x[1])
  if eval(f"r{go2}[{go1-1}] == '_'"):
    exec(f'r{go2}[{go1-1}] = symbol')
    continue1 = False
  else:
    continue1 = True
  if continue1 == True:
    print(Fore.RED + 'Someone is already there. please pick another slot.' + Fore.WHITE)
    continue
  if p1:
    playergo = 'p1'
  else:
    playergo = 'p2'
  goes += 1
  for i in lines:
    if collections.Counter(i)[symbol] == 3:
      print(Fore.GREEN + f'\n{playergo} wins!')
