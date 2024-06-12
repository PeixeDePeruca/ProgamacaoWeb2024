#it's a memory game,duh - https://media1.tenor.com/m/1BjnWiLaCOgAAAAC/girls-und-panzer-animation.gif

import random;
import os;
import time;
SortedNumber = int(0);
difficulty = int(0);
level = (1);
PlayerOption = int(0);


#print("\nWELCOME TO THE MEMORY GAME\n\nIn this game RANDOM NUMBERS will appear on screen," +
#      "all you have to do is remember these numbers and type them on the box below...\nare you good enough to reach level 10??🥸 🤔");

while ((difficulty < 1) or (difficulty > 3)):
    print("\nWELCOME TO THE MEMORY GAME!\n\nIn this game RANDOM NUMBERS will appear on screen," +
      "all you have to do is remember these numbers and type them on the box below...\nare you good enough to reach level 5??🥸 🤔\n");

    print("How's your memory?" + "\n" + "- Amnesia                         (1 = Easy😊)"
      + '\n' +'- I can remember stuff            (2 = Medium🥲 )' + '\n' + '- WW2 Veteran photographic memory (3 = Hard💀)\n')
    
    difficulty = int(input('Choose : '));
    
    if ((difficulty < 1) or (difficulty > 3)):
        print("\nChoose only the available options!");
        time.sleep(2)
        os.system("cls")
    else:
        time.sleep(2)
        os.system("cls")
    
level = difficulty
count = 4;

while(count >= 0):
    
    if(difficulty == 1):
        print("記憶ゲーム！- MEMORY GAME!\n");
        SortedNumber = random.randint(0 , 5);
    
    if(difficulty == 2):
        print("記憶ゲーム！- MEMORY GAME!\n");
        SortedNumber = random.randint(6 , 12);
    
    if(difficulty == 3):
        print("記憶ゲーム！- MEMORY GAME!\n");
        SortedNumber = random.randint(18 , 32);
   
    if(difficulty == 4):
        print("記憶ゲーム！- MEMORY GAME!\n");
        SortedNumber = random.randint(32 , 42);
    
    if(difficulty == 5):
        print("記憶ゲーム！- MEMORY GAME!\n");
        SortedNumber = random.randint(42 , 100);
    print (f"\nLevel = {level}\nMEMORIZE THE NUMBER:");
   
    print (SortedNumber);
    time.sleep(3);
    os.system("cls");
    
    PlayerOption = int(input('\nType a number: '));
    
    if(PlayerOption == SortedNumber):
        print(f"\nNICE,YOU REALLY HAVE A GOOD MEMORY😁👍\n")
        level = (level +1);
        difficulty = level
    else:
        if (count == 0):
            print("You're out of tries....GAME OVER!\n");
        else:
            print(f"\nHmm,your memory isn't that good,maybe you should see a doctor🤔\n You got more {count} tries...\n");
    
    if level > 5:
        print("GAME OVER!")
        break;
       

    count = (count - 1);
    

#numberGenerator():
#    contextChoice = random.randint(1 , 9);

#time.sleep(1)
#os.system("cls");








#while (difficulty != 1):
#    print("\nWELCOME TO THE MEMORY GAME\n\nIn this game RANDOM NUMBERS will appear on screen," +
 #     "all you have to do is remember these numbers and type them on the box below...\nare you good enough to reach level 10??🥸 🤔");

    
#numberGenerator = int("");

#random.randint(0 , 9);

#def gameplay(number)